import time
import random
import mouse
from pynput.keyboard import Controller
import win32api, win32con

movement = ["s", "a", "d", "w", "w", "a", "d", "w", "w"]


keyboard = Controller() 
time.sleep(5)
flipbit = 0
while(1):
    currentKey = int(random.uniform(0,8))
    keyboard.press(movement[currentKey])
    keyboard.press('f')
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 
            int(random.uniform(0,150)), 0, 0, 0)
    if(flipbit):
        for j in range(int(random.uniform(2,3))):
            mouse.click('left') 
            time.sleep(random.uniform(0,1))
    else
        keyboard.press('e')
    mouse.wheel(random.uniform(0,3))
    time.sleep(random.uniform(0, 4))
    keyboard.release(movement[currentKey])
    !flipbit
