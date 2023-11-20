# To run this, you need to remap the chat box to be something 
# other than the enter key otherwise you will type 'wasd' 
# throughout the match. Other than that, you should have default 
# keybindings.

import time
import random
import mouse
from pynput.keyboard import Controller, Key
import win32api, win32con


time.sleep(5)

movement = ["s", "a", "d", "w", "w", "a", "d", "w", "w"]
looking  = [1600, 500, 200, 25, 1200, 700, 800, 1000, 3000, 300]

Controller = Controller() 
flipbit = 0

while(1):
    # skip death cutscene or select gun on match startup
    Controller.press(Key.enter)
    Controller.release(Key.enter)
    Controller.press('f')
    Controller.release('f')

    # select random values for Controller presses and mouse movements
    currentKey = int(random.uniform(0, --len(movement)))
    currentLook = int(random.uniform(0, --len(looking)))

    # use the random values that were just selected
    Controller.press(movement[currentKey])
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 
            looking[currentLook], 0, 0, 0)
    
    # switch weapons
    mouse.wheel(random.uniform(0, 3))

    # decided if its time to throw a grenade or shoot
    if(flipbit):
        for j in range(int(random.uniform(1, 5))):
            mouse.click('left') 
            Controller.press('q')
            time.sleep(random.uniform(0,1))
            Controller.release('q')
    else:
        Controller.press('e')
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 0, 100, 0)
        Controller.release('e')
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 0, -100, 0)

    # sleeping allows for attempted map traversal while pressing movement[currentKey]
    time.sleep(random.uniform(0, 2))
    Controller.release(movement[currentKey])

    # flip the bit that determines whether you shoot or throw a grenade
    if(flipbit == 1):
        flipbit = 0
    elif (flipbit == 0):
        flipbit = 1
