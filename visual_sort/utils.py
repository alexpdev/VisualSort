import random
import string
from turtle import Screen
from time import time, sleep
from visual_sort import conf

def gen_color():
    return "#" + "".join([random.choice(string.hexdigits) for i in range(6)])

def screen_extend(screen):
    winHeight = screen.window_height()*.95
    winWidth = screen.window_width()*.95
    screen.halfh = winHeight / 2
    screen.halfw = winWidth / 2

def shuffle(stage):
    t = stage.screen.tracer()
    stage.screen.tracer(20)
    l = len(stage)
    choices = list(range(l))
    for i in range(3):
        for i in range(l):
            del choices[i]
            j = random.choice(choices)
            choices.insert(i,i)
            block1 = stage[i]
            block2 = stage[j]
            del stage[j]
            del stage[i]
            stage[i] = block2
            stage[j] = block1
    stage.screen.tracer(t)


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


def get_screen(screen_size, background, tracer, delay):
    screen = Screen()
    screen.setup(*screen_size)
    screen.bgcolor(background)
    screen.tracer(tracer)
    screen.delay(delay)
    winHeight = screen.window_height()*.95
    winWidth = screen.window_width()*.95
    screen.base = winHeight // 2
    blockWidth = screen.blockWidth = conf.BLOCK_WIDTH
    blockHeight = screen.blockHeight = conf.BLOCK_HEIGHT
    screen.start = -(winWidth // 2) + blockWidth
    screen.blocks = int((winWidth - ((blockWidth + 2) * 2)) // (blockWidth + 2))
    return screen
