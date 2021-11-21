import random
import string
from turtle import Screen
from time import time, sleep
try:
    from visual_sort import conf
except:
    import conf


cdict = {}
def colordict():
    for i in range(16):
        cdict[i] = string.hexdigits[i]
        cdict[string.hexdigits[i]] = i
    return cdict

def hextodec(string):
    if len(cdict) == 0:
        colordict()
    rgb, string = [], string[1:].lower()
    val = 0
    for _ in range(3):
        v = cdict[string[val]] * 16
        v += cdict[string[val+1]]
        rgb.append(v/255)
        val += 2
    return tuple(rgb)


def interpolateColor(color1, color2, factor=0.5):
    result = color1[:]
    for i in range(3):
        result[i] = result[i] + factor * (color2[i] - color1[i])
    return result


def interpolateColors(color1, color2, steps):
    stepFactor = 1 / (steps - 1)
    color1, color2 = [list(i) for i in [color1, color2]]
    for i in range(steps):
        yield interpolateColor(color1, color2, stepFactor * i)


def gradient(colors, blocks):
    step = gap = blocks // (len(colors) - 1)
    colors = [hextodec(color) for color in colors]
    for i in range(len(colors) - 1):
        c1 = colors[i]
        c2 = colors[i+1]
        for color in interpolateColors(c1,c2,gap+3):
            yield color


def randcolor():
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
    stage.screen.update()


def timer(func):
    def wrapper(stage):
        drawtitle(stage,Shuffle)
        Shuffle(stage)
        drawtitle(stage, func)
        then = time()
        func(stage)
        stage.screen.update()
        print(f"{func.__name__} Duration: {time() - then} seconds.")
        stage.screen.update()
        sleep(.5)
        stage.screen.update()
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
    screen.blocks = int(((screen.width * 2) - (screen.blockwidth*2))//(screen.blockwidth+1))
    screen.gradient = gradient(conf.GRADIENT, screen.blocks)
    return screen
