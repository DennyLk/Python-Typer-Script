import pyautogui
import time
import sys
import random
import string

# Complete mapping for each letter to nearby keys on a QWERTY keyboard
nearby_keys = {
    'a': ['q', 'w', 's', 'z'],
    'b': ['v', 'g', 'h', 'n'],
    'c': ['x', 'd', 'f', 'v'],
    'd': ['s', 'e', 'r', 'f', 'c', 'x'],
    'e': ['w', 's', 'd', 'r'],
    'f': ['d', 'r', 't', 'g', 'v', 'c'],
    'g': ['f', 't', 'y', 'h', 'b', 'v'],
    'h': ['g', 'y', 'u', 'j', 'n', 'b'],
    'i': ['u', 'j', 'k', 'o'],
    'j': ['h', 'u', 'i', 'k', 'm', 'n'],
    'k': ['j', 'i', 'o', 'l', 'm'],
    'l': ['k', 'o', 'p'],
    'm': ['n', 'j', 'k', 'l'],
    'n': ['b', 'h', 'j', 'm'],
    'o': ['i', 'k', 'l', 'p'],
    'p': ['o', 'l'],
    'q': ['w', 'a', 's'],
    'r': ['e', 'd', 'f', 't'],
    's': ['q', 'w', 'e', 'a', 'd', 'z', 'x'],
    't': ['r', 'f', 'g', 'y'],
    'u': ['y', 'h', 'j', 'i'],
    'v': ['c', 'f', 'g', 'b'],
    'w': ['q', 'a', 's', 'e'],
    'x': ['z', 's', 'd', 'c'],
    'y': ['t', 'g', 'h', 'u'],
    'z': ['a', 's', 'x'],
}

def type_into_vscode(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    time.sleep(3)  # Wait for you to focus VS Code

    start_time = time.time()  # Record the start time for pauses
    mistake_time = time.time()  # Record the start time for mistakes
    pause_counter = 0  # Initialize a counter to track the number of pauses

    for i, char in enumerate(content):
        current_time = time.time()  # Get the current time
        elapsed_time_since_pause = current_time - start_time  # Calculate elapsed time for pause
        elapsed_time_since_mistake = current_time - mistake_time  # Calculate elapsed time for mistake

        # Check if it's time to make a mistake
        if elapsed_time_since_mistake > 6 and char.lower() in nearby_keys:
            wrong_char = random.choice(nearby_keys[char.lower()])  # Choose a nearby key
            pyautogui.typewrite(wrong_char)  # Type the wrong character
            time.sleep(0.5)  # Short pause to mimic human correction speed
            pyautogui.press('backspace')  # Delete the wrong character
            mistake_time = time.time()  # Reset the mistake timer

        # Check if it's time to take a pause
        if elapsed_time_since_pause > 5:
            # Determine the pause duration based on the current value of pause_counter
            pause_duration = [2, 1, 1.5, 2.5][pause_counter % 4]
            time.sleep(pause_duration)  # Pause for the determined duration
            pause_counter += 1  # Increment the pause counter
            start_time = time.time()  # Reset the pause timer

        pyautogui.typewrite(char)  # Type the correct character

        # Halve the delay if the character is a space or newline
        delay = random.uniform(0, 0.2) / 2 if char in [' ', '\n'] else random.uniform(0, 0.2)
        time.sleep(delay)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <code2.txt>")
        sys.exit(1)

    file_path = sys.argv[1]
    type_into_vscode(file_path)
