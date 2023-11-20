import time
import random
import mouse
from pynput.keyboard import Controller, Key
import win32api, win32con


time.sleep(5)

movement = ["s", "a", "d", "w", "w", "a", "d", "w", "w"]
looking  = [1600, 500, 200, 25, 1200, 700, 800, 1000, 3000, 300]

keyboard = Controller() 
flipbit = 0

while(1):
    # skip death cutscene or select gun on match startup
    keyboard.press(Key.enter)
    keyboard.press('f')
    keyboard.release(Key.enter)
    keyboard.release('f')

    # select random values for keyboard presses and mouse movements
    currentKey = int(random.uniform(0, --len(movement)))
    currentLook = int(random.uniform(0, --len(looking)))

    # use the random values that were just selected
    keyboard.press(movement[currentKey])
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 
            looking[currentLook], 0, 0, 0)
    
    # switch weapons
    mouse.wheel(random.uniform(0, 3))

    # deploy equipment
    keyboard.press('x')
    keyboard.release('x')

    # decided if its time to throw a grenade or shoot
    if(flipbit == 1):
        for j in range(int(random.uniform(1, 5))):
            mouse.click('left') 
            keyboard.press('q')
            time.sleep(random.uniform(0,1))
            keyboard.release('q')
    else:
        keyboard.press('e')
        time.sleep(random.uniform(0,1))
        keyboard.release('e')

    # sleeping allows for attempted map traversal while pressing movement[currentKey]
    time.sleep(random.uniform(0, 2))
    keyboard.release(movement[currentKey])

    # flip the bit that determines whether you shoot or throw a grenade
    if(flipbit == 1):
        flipbit = 0
    else:
        flipbit = 1
