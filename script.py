import time
import random
import mouse
from pynput.keyboard import Controller
import win32api, win32con

movement = ["s", "a", "d", "w", "w", "a", "d", "w", "w"]
keyboard = Controller() 

time.sleep(5)

while(1):
    currentKey = int(random.uniform(0,8))
    keyboard.press(movement[currentKey])
    keyboard.press('f')
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(random.uniform(0,1600)), int(random.uniform(0,720)), 0, 0)
    for j in range(int(random.uniform(10,20))):
        mouse.click('left') 
        time.sleep(random.uniform(0,1)
    mouse.wheel(random.uniform(0,3))
    time.sleep(random.uniform(0, 2))
    keyboard.release(movement[currentKey]
