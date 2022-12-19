from PIL import ImageGrab

print("load grabimg")

def catchIMG():
    screen = ImageGrab.grab()
    return screen


