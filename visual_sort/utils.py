import random
import string
from turtle import Screen
from time import time, sleep
from visual_sort import conf

def gen_color():
    return "#" + "".join([random.choice(string.hexdigits) for i in range(6)])

def Shuffle(stage):
    l = len(stage)
    choices = list(range(l))
    for turn in range(2):
        for i1 in range(l):
            i2 = l - i1 - 1
            x = random.choice(choices)
            y = random.choice(choices)
            swap(stage, i1, y)
            swap(stage, i2, x)

def swap(stage, i, j):
    block1 = stage[i]
    block2 = stage[j]
    stage[i] = block2
    stage[j] = block1

def drawtitle(stage, func):
    pen = stage.pen
    pen.clear()
    font = ("Century", 34, "normal")
    name = func.__name__
    stage.pen.write(name, move=False, align="center", font=font)

def timer(func):
    def wrapper(stage):
        t,d = stage.screen.tracer(), stage.screen.delay()
        drawtitle(stage,Shuffle)
        Shuffle(stage)
        if func.__name__ == "CycleSort":
            stage.screen.tracer(3)
            stage.screen.delay()
        drawtitle(stage, func)
        then = time()
        func(stage)
        print(f"{func.__name__} Duration: {time() - then} seconds.")
        stage.screen.tracer(t)
        stage.screen.delay(d)
        sleep(.5)
        return stage
    return wrapper

def get_screen():
    screen = Screen()
    screen.setup(*conf.SCREEN_SIZE)
    screen.bgcolor(conf.BACKGROUND)
    screen.tracer(conf.TRACER)
    screen.delay(conf.DELAY)
    screen.title(conf.TITLE)
    screen.speed = conf.SPEED
    screen.winheight = screen.window_height()*.95
    screen.winwidth = screen.window_width()*.95
    screen.width = screen.winwidth // 2
    screen.height = screen.winheight // 2
    screen.blockwidth = conf.BLOCK_WIDTH
    screen.increment = screen.blockheight = conf.BLOCK_HEIGHT
    screen.base = screen.height
    screen.start = -screen.width + screen.blockwidth
    screen.blocks = int(((screen.width * 2) - ((screen.blockwidth + 2)*3))//(screen.blockwidth + 2))
    return screen
