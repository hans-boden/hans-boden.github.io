# python3
"""
    Show the usage of the gui4image_z module
"""

import time
import random
from PIL import Image
from gui4image_z import DynamicDisplay

size = dimx, dimy = 150, 100
bgcor = (255,255,255)
fgcor = (0,50,120)

colors = ((250,0,0), (0,250,0), (0,0,250),
          (150,150,0), (150,0,150), (0,150,150),
          (180,180,180), (50,50,50), (220,220,0))

def main():
    print("main starts")
    
    im = Image.new("RGB", size, bgcor)
    
    pix = im.load()
    gui = DynamicDisplay(im, zoom=8, fps=16, title="Gui Sample App")

    draw_something(pix)

    time.sleep(0.5)
    im.completed = True

    print("main ends")


def draw_something(pix):

    while True:
        time.sleep(0.02)
        x = random.randint(4 ,dimx-5)
        y = random.randint(4, dimy-5)
        cor = random.choice(colors)
        pix[x,y] = cor

    
if __name__ == '__main__':
    main()
