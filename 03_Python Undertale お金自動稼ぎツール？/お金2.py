import pyautogui
import pyperclip
import time
import random

pyautogui.click(1000,500)
time.sleep(2.10)
for i in range(2):
    a=0
    b=0
    pyautogui.hotkey('z','t')
    num = random.uniform(0.1,0.2)
    time.sleep(num)
    pyautogui.hotkey('down','t')
    num = random.uniform(0.1,0.2)
    time.sleep(num)
    for i in range(16):
        a+=1
        pyautogui.hotkey('z','t')
        num = random.uniform(0.1,0.2)
        time.sleep(num)
    time.sleep(1.00)
    pyautogui.hotkey('x','t')
    num = random.uniform(0.1,0.2)
    time.sleep(num)
    pyautogui.hotkey('down','t')
    num = random.uniform(0.1,0.2)
    time.sleep(num)
    for i in range(17):
        b+=1
        pyautogui.hotkey('z','t')
        num = random.uniform(0.1,0.2)
        time.sleep(num)
    pyautogui.hotkey('up','t')
    num = random.uniform(0.1,0.2)
    time.sleep(num)
    print(a)
    print(b)
#つしまの勝ち！
