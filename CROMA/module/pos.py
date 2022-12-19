import pyautogui as pag
from . import grabimg
import time

print("load pos")

def returnScreen():
    screen = grabimg.catchIMG()
    pos = pag.position()
    print(pos)

    return screen.getpixel(pos)

print("loading...")
time.sleep(1)
print("Done")
time.sleep(1)
print("Start =")
print("Stop  -")
print("EXIT  ]")
time.sleep(1)