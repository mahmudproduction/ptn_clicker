import pyautogui
import keyboard
import time
# screenWidth, screenHeight = pyautogui.size()

# print (screenWidth, screenHeight )


# currentMouseX, curreentMouseY = pyautogui.position()


# print(currentMouseX, curreentMouseY)


def clicka():
    a= 31
    while a>0:
        funu = pyautogui.click()
        print (f'{a}click')
        a -= 1
    return funu 

keyboard.add_hotkey('ctrl+alt+b', lambda:clicka())

# # 

# # # Block forever, like `while True`.
keyboard.wait()
  
