import random
import string
from turtle import Screen
from time import time, sleep
from visual_sort import conf

def gen_color():
    return "#" + "".join([random.choice(string.hexdigits) for i in range(6)])

def shuffle(stage):
    l = len(stage)
    choices = list(range(l))
    for i in range(3):
        for i in range(l):
            j = random.choice(choices)
            block1 = stage[i]
            block2 = stage[j]
            stage[i] = block2
            stage[j] = block1

def timer(func):
    def wrapper(stage):
        stage = stage
        shuffle(stage)
        then = time()
        func(stage)
        print(f"{func.__name__} Duration: {time() - then} seconds.")
        sleep(.8)
        return stage
    return wrapper

def get_screen():
    screen = Screen()
    screen.setup(*conf.SCREEN_SIZE)
    screen.bgcolor(conf.BACKGROUND)
    screen.tracer(conf.TRACER)
    screen.delay(conf.DELAY)
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
