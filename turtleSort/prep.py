# -*- encoding utf8-*-
# turtleSort.utils.prep
from turtle import Screen
import random

from turtleSort.config import OPTIONS
from turtleSort.classes import Location, Section


def gen_color_random(units):
    start = 0
    while start < units:
        nums = list(range(1,255,10))
        colors = [random.choice(nums) for i in range(3)]
        yield tuple(colors)
        start += 1

def gen_gradient(start,end,units):
    incs = [(end[i]-start[i])/units for i in range(len(start))]
    zed,last = 0,list(start)
    while zed < units:
        for i,x in enumerate(incs):
            last[i] += x
        yield tuple([int(i) for i in last])
        zed += 1

def gen_screen(**kwargs):
    screen = Screen()
    # colormode: 0 or 255
    screen.colormode(kwargs["colormode"])
    # background screen color
    screen.bgcolor(kwargs["bgcolor"])
    # tracer and delay values
    screen.tracer(kwargs["tracer"],kwargs["delay"])
    return screen

def screen_size(screen,**kwargs):
    x1,y1 = kwargs["size"]
    px,py = kwargs["s_pos"]
    screen.setup(x1,y1,px,py)
    x,y = ((screen.window_width())*.95)//2,((screen.window_height())*.97)//2
    units = x*2//kwargs["width"]
    return (x,y,units)

def color_method(units,**kwargs):
    if kwargs["random"]:
        return gen_color_random(units)
    color1,color2 = kwargs["gradient"]
    colors = gen_gradient(color1,color2,units)
    return colors

def setup(**kwargs):
    if not kwargs:
        kwargs = OPTIONS
    screen = gen_screen(**kwargs)
    x,y,units = screen_size(screen,**kwargs)
    colors = color_method(units,**kwargs)
    start,seq,value = -x,[],kwargs["inc"]
    while start < x:
        _keys = get_kws(value,colors,**kwargs)
        loc = Location((start,-y),len(seq))
        sect = Section.create(screen,**_keys)
        loc.assign(sect)
        seq.append(loc)
        start += kwargs["gap"]
        value += kwargs["inc"]
    for loc in seq:
        loc.draw()
    return seq,screen

def get_kws(value,colors,**kwargs):
    _keys = {}
    _keys["color"] = next(colors)
    _keys["value"] = value
    _keys["speed"] = kwargs["speed"]
    _keys["width"] = kwargs["width"]
    if not kwargs["tracer"] and not kwargs["delay"]:
        _keys["trace"] = False
    else:
        _keys["trace"] = True
    return _keys
