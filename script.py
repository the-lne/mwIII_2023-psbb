import time
import random
import mouse
from pynput.keyboard import Controller
keyboard = Controller() 


#init (get mouse position)
#begin loop

#issues: figure out how to determine whether a game is going or not

#mouse.get_position()
#mouse.move(125, 50)
#mouse.move(150, 150, duration = 1.0)
#mouse.click('left') 
#mouse.click('right')    
#mouse.click('middle')   
#mouse.wheel(5)
#mouse.wheel(-3)


movement = ["s", "a", "d", "w", "w", "a", "d", "w", "w"]

# begin loop! 
time.sleep(5)
#for i in range(1,10):
while(1):
    currentKey = int(random.uniform(0,8))
    keyboard.press(movement[currentKey])
    keyboard.press('f')
    for j in range(int(random.uniform(10,20))):
        mouse.click('left') 
    mouse.wheel(random.uniform(0,3))
    time.sleep(random.uniform(0, 2))
    keyboard.release(movement[currentKey])
