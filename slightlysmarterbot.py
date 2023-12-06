# call of duty modern warfare 3 (2023) player sbmm counterbalancing bot

import time
import random
import mouse
from pynput.keyboard import Controller, Key
import win32api, win32con
import os
import pyscreenshot as ImageGrab
import cv2
import numpy as np


# Because these values are accessed randomly (by using array[int(random.uniform(0, --len(array)))]
# notice how we select from range 0 to length of array -1), multiple indicies have the same value 
# to increase the likelihood that it is chosen.
movement = ["s", "a", "d", "w", "w", "a", "d", "w", "w"]
looking  = [1600, 500, 200, 25, 1200, 700, 800, 1000, 3000, 300]
throwables = ["e", "q", "e"]
keyboard = Controller() 


# returns True if two screen shots are the same, indicating that, yes, the player is stuck.
# the way screen shots are compared is weird and sloppy, basically, the screenshots are 
# edited down to small 10px squares, if they have the same colors, they are deemed to be 
# the same picture.
def iamstuck():
    im1 = ImageGrab.grab()
    im2 = ImageGrab.grab()

    im1 = ImageGrab.grab(bbox=(25,25,35,35))
    im1.save('old.png')

    im2 = ImageGrab.grab(bbox=(25,25,35,35))
    im2.save('current.png')

    if ((cv2.cvtColor(cv2.imread('old.png'), cv2.COLOR_BGR2HSV) == 
            cv2.cvtColor(cv2.imread('current.png'), cv2.COLOR_BGR2HSV)).all() == True):
        print("is not moving")
        os.system('cmd /c "del old.png"') 
        os.system('cmd /c "del current.png"')
        return True
    else:
        print("is moving")
        os.system('cmd /c "del old.png"') 
        os.system('cmd /c "del current.png"')
        return False

# if iterator is even, use throwables, for odd, shoot
def shootemgungumstyle(iterator):
    mouse.wheel(random.uniform(0, 3))
    if(iterator % 2 ) == 0:
        currentThrowable = int(random.uniform(0, --len(throwables)))
        keyboard.press(throwables[currentThrowable])
        time.sleep(0.1)
        keyboard.release(throwables[currentThrowable])
    else:
        for j in range(0, 3):
            mouse.click('left')
            time.sleep(0.1)


# when iamstuck() returns True, this function is called in an attempt to traverse the map
def movementProtocol():
    i = 0
    total = int(random.uniform(1, 3))
    while(i <= total):
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 
                looking[int(random.uniform(0, --len(looking)))], 0, 0, 0)
        shootemgungumstyle(i)
        time.sleep(random.uniform(1, 2))
        # i++ seriously doesn't work in python?? sacrilege! 
        i = i+1
    return


# 5 second delay before the program begins
time.sleep(5)

while(1):
    keyboard.press('w')
    print("on main loop")
    if(iamstuck()):
        keyboard.release('w')
        currentKey = int(random.uniform(0, --len(movement)))
        keyboard.press(movement[currentKey])
        movementProtocol()
        time.sleep(random.uniform(0, 2))
        keyboard.press(Key.space)
        keyboard.release(movement[currentKey])
        keyboard.release(Key.space)
