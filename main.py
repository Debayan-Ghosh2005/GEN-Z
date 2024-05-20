import os
import eel
from chat import *

def start():
    try:
        print("Initializing Eel...")
        eel.init('UI')
        print("Opening Microsoft Edge...")
        os.system('start chrome.exe --app="http://localhost:8000/index.html"')
        print("Starting Eel application...")
        eel.start('index.html', mode=None, host='localhost', block=True)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    start()