from win32 import win32print
import pyautogui
distance = 300
pyautogui.PAUSE = 2.5
pyautogui.click()
while distance > -100:
        pyautogui.dragRel(distance, 0, duration=0)   # move right
        distance -= 5
        pyautogui.dragRel(0, distance, duration=0)   # move down
        pyautogui.dragRel(-distance, 0, duration=0)  # move left
        distance -= 5
        pyautogui.dragRel(0, -distance, duration=0)  # move up
