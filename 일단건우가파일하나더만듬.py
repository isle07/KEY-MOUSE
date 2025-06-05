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

while 1:
    pyautogui.click(x=600,y=400)
    time.sleep(0.1)
    pyautogui.doubleClick(x=650,y=450)
    time.sleep(0.1)