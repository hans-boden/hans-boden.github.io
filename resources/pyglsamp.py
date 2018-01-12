#python3
"""
    experiment with pyglight drawing module
"""

import pyglight as pgl
from pyglet.window import key as pwkey
import time
import random

cortab = pgl.cortab
light_grey = pgl.add_color(210,210,210)
dimx, dimy = 120, 90 # dimensions in 'pixel'

blue =pgl.color.blue

    
def main():
    pgl.register_cb(pwkey.X, cb_x)  # register a short time function
    pgl.register_thread(pwkey.R, cb_thread) # register a long running thread

    pgl.start(dimx, dimy)

def cb_x(symb):
    print("'x' was pressed")
    size = 8
    for x in range(0,8):
        for y in range(0,8):
            cx = 8*x+y
            px, py = x*(size+1), y*(size+1)
            for tx in range(px, px+size):
                for ty in range(py,py+size):
                    pgl.setpixel(tx,ty,cx)
    px += 10
    py += 10
    cx = pgl.color.green # upper right corner
    for tx in range(px, px+size):
        for ty in range(py,py+size):
            pgl.setpixel(tx,ty,cx)


def cb_thread():
    for _ in range(9000):
        x = random.randint(0, dimx-1)
        y = random.randint(0, dimy-1)
        new = random.randint(0, len(pgl.cortab)-1)
        old = pgl.getpixel(x,y)
        if old != 0: # empty = black = 0
            new = light_grey
        pgl.setpixel(x,y,new)
        time.sleep(0.01)

        
main()
