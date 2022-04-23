import pyautogui

pyautogui.moveTo(1000,300, duration=1)
pyautogui.PAUSE = 0.01

for i in range(1000):
    pyautogui.click(1000,300)