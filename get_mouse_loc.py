#please install pyautogui if:ModuleNotFoundError: No module named 'pyautogui'
#use pip install pyautogui

import pyautogui
x, y = pyautogui.position()
print(str(x) + "," + str(y))
