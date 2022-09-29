import time
import datetime
import pyautogui
while True:
    x = datetime.datetime.now()
    y = x.strftime("%d_%m_%Y_%H_%M_%S_%f")
    pyautogui.screenshot(r"C:\Users\akmet\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\ss\ss{}.png".format(y))
    time.sleep(20)