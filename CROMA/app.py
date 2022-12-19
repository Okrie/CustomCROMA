
from PIL import ImageGrab
import time
import sys
import pyautogui as pag
import keyboard
import random
import threading as th
from pynput import keyboard
from pynput.keyboard import Key, Controller, KeyCode
from module import grabimg, pos

kbControl = Controller()

def loading():
    print('Start...ing')
    time.sleep(1)
    while running :
        screen = ImageGrab.grab()
        ok_rgb = (255,210,0)
        dungeon_ok_rgb = (101,121,135)
        tel_ok_rgb = (101,121,135)

        pos = (1826,846)
        dungeon_pos = (1019, 659)
        tel_pos = (971, 646)

        dungeon_rgb = screen.getpixel(dungeon_pos)
        rgb = screen.getpixel(pos)
        tel_rgb = screen.getpixel(tel_pos)

        if tel_ok_rgb == tel_rgb :
            com_pos=(971, 641)
            time.sleep(random.uniform(0.1,0.3))
            pag.mouseDown(com_pos)
            time.sleep(random.uniform(0.1,0.3))
            pag.mouseUp(com_pos)
            time.sleep(random.uniform(0.1,0.3))

        if dungeon_ok_rgb == dungeon_rgb :
            com_pos=(1019, 659)
            time.sleep(random.uniform(0.1,0.3))
            pag.mouseDown(com_pos)
            time.sleep(random.uniform(0.1,0.3))
            pag.mouseUp(com_pos)
            time.sleep(random.uniform(10,12))
            com_pos=(1824,141)
            time.sleep(random.uniform(0.1,0.3))
            pag.mouseDown(com_pos)
            time.sleep(random.uniform(0.1,0.3))
            pag.mouseUp(com_pos)
            time.sleep(random.uniform(0.1,0.3)) 

        if not rgb == ok_rgb :
            com_pos=(1824,141)
            time.sleep(random.uniform(0.1,0.3))
            pag.mouseDown(com_pos)
            time.sleep(random.uniform(0.1,0.3))
            pag.mouseUp(com_pos)
            time.sleep(random.uniform(0.1,0.3))

        if rgb == ok_rgb :
            time.sleep(random.uniform(1.0,2.0))
        
def on_press(key):
    global running  # inform function to assign (`=`) to external/global `running` instead of creating local `running`
    try:
        if key == keyboard.KeyCode(char='='):
            running = True
            print(f'Start')
            # create thread with function `loading`
            t = th.Thread(target=loading)
            # start thread
            t.start()
            
        if key == keyboard.KeyCode(char='-'):
            print(f'Stop')
            # to stop loop in thread
            running = False

        if key == keyboard.KeyCode(char=']'):
            print(f'Exit Program')
            sys.exit()
            return False
    except KeyboardInterrupt:
        print(f'{key}')

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

    