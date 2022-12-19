
from PIL import ImageGrab
import time
import pyautogui as pag
import keyboard
import random
from pynput.keyboard import Key, Listener
from pynput import keyboard
import threading as th
# from pynput.keyboard import Key, Controller, KeyCode
from module import grabimg, pos

keep_going = False

def on_press(key, abortKey = '-'):
    try:
        if key == keyboard.KeyCode(char='='):
            print(f'Start')
            keep_going = True
            __main__()
            
        if key == keyboard.KeyCode(char='-'):
            print(f'End')
            return False
        
    except AttributeError:
        print(f'{key}')
        
    if key == abortKey:
        print(f'End...')
        sys.exit()       

def __main__():
    while keep_going :
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

    
if __name__ == '__main__':
    import sys
    print('Start...ing')
    abortKey = '-'
    listener = keyboard.Listener(on_press=on_press, abortKey=abortKey)
    listener.start()  # start to listen on a separate thread
    
    listener.join()
    if keep_going == True:
        th.Thread(target=__main__, args=(), name='__main__', daemon=True).start()
    #listener.join()
