import os
import sys
import random
from turtle import Screen, RawTurtle
from time import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from temp.config import OPTIONS
from temp.sorting import (bubblesort,cyclesort,selectionsort,
                          insertionsort,mergesort,quicksort)

def gen_color():
    choices = ["1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F"]
    random.shuffle(choices)
    color = "#"
    for i in range(3):
        char = random.choice(choices)
        color += char
        choices.remove(char)
        random.shuffle(choices)
    return color

class Bar(RawTurtle):

    def __init__(self,window,stage,value=None):
        RawTurtle.__init__(self,window.screen)
        self.stage = stage
        self.window = window
        self.screen = window.screen
        self.value = value
        self.color(gen_color())
        self.speed(0)
        self.ht()
        self.up()

    def __str__(self):
        return f"({self.idx},{self.value})"

    def __repr__(self):
        return str(self)

    def copy(self):
        bar = Bar(self.window,self.stage,self.value)
        bar.setposition(self.idx)
        return bar

    def remove(self):
        self.clear()
        self.up()

    def setposition(self,idx):
        self.idx = idx
        self.up()
        return

    def corners(self):
        x1,x2 = self.stage[self.idx]
        x1, x2 = x1 + 1, x2 - 1
        y1 = -self.window.height
        y2 = y1 + self.value
        corners = ((x1,y1),(x2,y1),(x2,y2),(x1,y2))
        return corners

    def draw(self):
        corners = self.corners()
        self.goto(corners[0])
        self.down()
        self.begin_fill()
        for i in corners:
            self.goto(i)
        self.end_fill()
        self.up()

class Stage(list):
    def __init__(self,*args):
        super(list,self).__init__(*args)
        self.vals = []

    def drawstage(self,corners,color,window):
        self.window = window
        self.bar = Bar(self.window,self)
        self.bar.up()
        self.bar.ht()
        self.bar.color(color)
        self.bar.goto(corners[0])
        self.bar.down()
        self.bar.begin_fill()
        for corner in corners:
            self.bar.goto(corner)
        self.bar.end_fill()

    def fill_positions(self,width,height,dist,inc):
        start,counter = -width,1
        while start < width:
            n = start + dist
            val = inc * counter
            self.append((start,n))
            bar = Bar(self.window,self,val)
            idx = len(self)
            bar.setposition(idx-1)
            self.vals.append(bar)
            counter += 1
            start = n
        for pos in self.vals:
            pos.draw()

    def clear_stage(self):
        for bar in self.vals:
            bar.remove()

    def swap(self,val1,val2):
        bar1 = self.vals[val1]
        bar2 = self.vals[val2]
        self.vals[val1] = bar2
        bar2.setposition(val1)
        self.vals[val2] = bar1
        bar1.setposition(val2)
        return bar1,bar2

    def redraw(self,bar1,bar2):
        bar1.remove()
        bar2.remove()
        bar1.draw()
        bar2.draw()
        return

    def shuff_x(self,x):
        for i in range(x):
            self.shuffle()


    def shuffle(self):
        self.window.set_tracer(25)
        choices = list(range(len(self)))
        while len(choices) > 1:
            num1 = random.choice(choices)
            choices.remove(num1)
            num2 = random.choice(choices)
            choices.remove(num2)
            b1,b2 = self.swap(num1,num2)
            self.redraw(b1,b2)
        self.window.reset_tracer()
        return

class Window:

    def __init__(self,size=None,inc=None,bgcolor=None,tracer=None,dist=12):
        self.screen = Screen()
        self.screen.setup(*size)
        self.win_height = self.screen.window_height()*.95
        self.win_width = self.screen.window_width()*.95
        self.height = self.win_height / 2
        self.width = ((self.win_width//dist)*dist)/2
        self.dist = dist
        self.inc = inc
        self._tracer = tracer
        self.screen.bgcolor(bgcolor)
        self.screen.tracer(tracer)
        self.create_stage(dist)

    def set_tracer(self,num):
        self.screen.tracer(num)

    def reset_tracer(self):
        self.screen.tracer(self._tracer)

    def create_stage(self,d):
        self.stage = Stage()
        width = self.width
        height = self.height
        stage_corners = [(-width-6,-height),(-width,-height-18),
                         (width,-height-18),(width+6,-height)]
        stage_color = gen_color()
        self.stage.drawstage(stage_corners,stage_color,self)
        self.stage.fill_positions(self.width,self.height,self.dist,self.inc)

def setup(**kwargs):
    window = Window(**kwargs)
    window.stage.shuff_x(2)
    bubblesort(window.stage)
    window.stage.shuff_x(2)
    cyclesort(window.stage)
    window.stage.shuff_x(2)
    selectionsort(window.stage)
    window.stage.shuff_x(2)
    insertionsort(window.stage)
    window.stage.shuff_x(2)
    mergesort(window.stage)
    window.stage.shuff_x(2)
    quicksort(window.stage)
    window.stage.shuff_x(2)

    window.screen.mainloop()




setup(**OPTIONS)
