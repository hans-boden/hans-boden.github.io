# python3
"""
    use pyglet for simple pixel drawings
"""

import pyglet
from pyglet import window, clock, font
import pyglet.gl as gl
import time
import random
import threading

pwkey = pyglet.window.key

color_range = cr = 3
cortab = [(r/cr, g/cr, b/cr, 1.0)
          for r in range(cr+1) for g in range(cr+1) for b in range(cr+1)]

default_color = 0

class color():
    white=63
    yellow=60
    red=48
    brown=36
    black=0
    blue=7
    green=8
    grey=21
    pink=50
    orange=52
    
class G():
    dimx, dimy = 0, 0
    cell_size = 10
    cell_fill = cell_size - 1

    cols, rows = 0, 0
    grid = []

    vertlist = []  # permanent vertex list, which is updated in place
    
    callback_funcs = {}
    callback_thread = [None, None]
    thread_running = False

        
#print("window: {},{}".format(G.dimx, G.dimy))

def main(cols=80, rows=60, cell=10):
    G.cols, G.rows = cols, rows
    G.cell_fill = cell - 1
    assert G.cell_fill > 1
    G.cell_size = cell
    G.dimx, G.dimy = cols*cell, rows*cell
    
    mywin = pyglet.window.Window(G.dimx, G.dimy, resizable=False)
    #mywin.set_minimum_size(320, 200)
    #mywin.set_maximum_size(1400, 900)
    
    pyglet.clock.schedule_interval(draw_prepared_vertex, 0.05)
    
    @mywin.event
    def on_draw():
        #print('on_draw event')
        draw_prepared_vertex(0)

    @mywin.event
    def on_resize(ndimx, ndimy):
        print('on_resize event: {},{}'.format(ndimx, ndimy))
        G.dimx, G.dimy = ndimx, ndimy
        G.cols, G.rows = [x // G.cell_size for x in (ndimx, ndimy)]

        G.grid = [[default_color for y in range(G.rows)] for x in range(G.cols)]
        print("grid_size = x:{}, y:{}".format(G.cols, G.rows))
        
        prepare_vertex_list()

    @mywin.event  # internally adds the event handler instead of replacing it
    #             # the default handler reacts on [esc] with closing the window
    def on_key_press(symbol, modifiers):
        if symbol in G.callback_funcs:
            #print('A cb key was pressed.')
            G.callback_funcs[symbol](symbol)
            #print("back from callback")

        elif symbol == G.callback_thread[0]:
            start_callback_thread()

    pyglet.app.run()

start = main

def add_color(r,g,b):
    ndx = len(cortab)
    cortab.append((r/255, g/255, b/255, 1.0))
    return ndx

def get_dimensions():
    return G.cols, G.rows

def register_cb(key, fn):
    G.callback_funcs[key] = fn
    
def register_thread(key, fn):
    if G.thread_running:
        print("register_tread() disabled, thread already running")
    else:
        G.callback_thread = [key, fn]

def setpixel(x,y, cor):
    G.grid[x][y] = cor
    r, g, b, a = cortab[cor]
    pos = 12 * (x + G.cols * y)
    G.vertlist.colors[pos:pos+12] = [r,g,b,r,g,b,r,g,b,r,g,b]

def getpixel(x,y):
    if 0 <= x < G.cols and 0 <= y < G.rows:
        return G.grid[x][y]

def start_callback_thread():
    if G.thread_running:
        print("calling of thread disabled, already running")
    else:
        G.thread_running = True
        t = ThreadRunner()
        t.start()
        print("ThreadRunner is started")

class ThreadRunner(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("ThreadRunner starts")
        G.callback_thread[1]()
        G.thread_running = False
        print("ThreadRunner ended")

def prepare_vertex_list():
    vertices = []
    colors = []
    for x,y in ((x,y) for y in range(G.rows) for x in range(G.cols)):
        set_vertex_data(vertices, colors, x,y)
    G.vertlist = pyglet.graphics.vertex_list(len(vertices) // 2,
                        ('v2i/static', vertices), ('c3f/dynamic', colors))
    
def draw_prepared_vertex(dt):
    G.vertlist.draw(gl.GL_QUADS)

def set_vertex_data(vert_list, cor_list, x, y ):
    corid = G.grid[x][y]
    r, g, b, a = cortab[corid]
    ofsx, ofsy = x * G.cell_size, y * G.cell_size
    x1, y1, x2, y2 = ofsx, ofsy, ofsx + G.cell_fill, ofsy + G.cell_fill
    vert_list.extend((x1, y1, x1, y2, x2, y2, x2, y1))
    cor_list.extend((r, g, b, r, g, b, r, g, b, r, g, b))
    
print("module= {}".format(__name__))          
if __name__ == "__main__":
    main()

