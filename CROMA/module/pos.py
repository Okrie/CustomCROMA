import pyautogui as pag
from . import grabimg

print("load pos")

def returnScreen():
    screen = grabimg.catchIMG()
    pos = pag.position()
    print(pos)

    return screen.getpixel(pos)
