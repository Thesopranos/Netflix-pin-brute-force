# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 17:40:59 2022

@author: Mertcan
"""
import pyautogui
from time import sleep

bas1 = 0
bas2 = 0
bas3 = 0
bas4 = 0

while True:
    if bas4 == 9:
        bas4 = 0
        if bas3 == 9:
            bas3 = 0
            if bas2 == 9:
                bas2 = 0
                if bas1 == 9:
                    break
                else:
                    bas1 += 1
            else:
                bas2 += 1
        else:
            bas3 += 1
    else:
        bas4 += 1
    pyautogui.typewrite(str(bas1))
    pyautogui.typewrite(str(bas2))
    pyautogui.typewrite(str(bas3))
    pyautogui.typewrite(str(bas4))
    print(f"{bas1}{bas2}{bas3}{bas4}")
    sleep(0.05)