import pyautogui
import time
import sys

def type_into_vscode(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    time.sleep(5)  # Wait for you to focus VS Code

    for char in content:
        pyautogui.typewrite(char, interval=0.5)  # Type with a delay

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <code.txt>")
        sys.exit(1)

    file_path = sys.argv[1]
    type_into_vscode(file_path)
mamacita