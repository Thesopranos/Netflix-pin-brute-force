# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:40:59 2022

@author: Mertcan
"""
import pyautogui
from time import sleep

bas = {1: 0, 2: 0, 3: 0, 4: 0}

sleep(5)

while True:
    if bas[4] == 9:
        bas[4] = 0
        if bas[3] == 9:
            bas[3] = 0
            if bas[2] == 9:
                bas[2] = 0
                if bas[1] == 9:
                    break
                else:
                    bas[1] += 1
            else:
                bas[2] += 1
        else:
            bas[3] += 1
    else:
        bas[4] += 1
    pyautogui.typewrite(str(bas[1]))
    pyautogui.typewrite(str(bas[2]))
    pyautogui.typewrite(str(bas[3]))
    pyautogui.typewrite(str(bas[4]))
    print(f"{bas[1]}{bas[2]}{bas[3]}{bas[4]}")