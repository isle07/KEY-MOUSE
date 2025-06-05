import pyautogui
import keyboard
import time
#asdf
while 1:
    position = pyautogui.position()
    if keyboard.is_pressed('enter'):
        print(position)
        time.sleep(0.2)
        import pyautogui
import time