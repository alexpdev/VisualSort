# -*- encoding utf8-*-
# turtleSort.utils.prep
from classes import Location, Section, OPTIONS
from turtle import Screen
import random

def gen_color_random():
    start = 0
    while start < 200:
        nums = list(range(1,255,10))
        colors = [random.choice(nums) for i in range(3)]
        yield tuple(colors)

def gen_gradient(start,end):
    common,counts,zed,lstart = [],[0,0,0],0,list(start)
    for x,y in zip(start,end):
        if x > 255 or y > 255: raise Exception
        val = abs(y - x)/120
        common.append(val)
    while zed < 100:
        last = counts[:]
        for j,k in enumerate(common):
            counts[j] += k
            lstart[j] += k
        if [i for i in range(3) if abs(counts[i]-last[i]) > 1]:
            yield tuple([int(i) for i in lstart])
            zed += 1

def gen_screen(**kwargs):
    screen = Screen()
    # colormode: 0 or 255
    if "colormode" in kwargs:
        screen.colormode(kwargs["colormode"])
    else:
        screen.colormode(255)
    # background screen color
    if "bgcolor" in kwargs:
        screen.bgcolor(kwargs["bgcolor"])
    else:
        screen.bgcolor("black")
    # tracer and delay values
    if "tracer" in kwargs:
        if "delay" in kwargs:
            screen.tracer(kwargs["tracer"],kwargs["delay"])
        else:
            screen.tracer(kwargs["tracer"])
    else:
        screen.tracer(1,0)
    return screen

def screen_size(screen,**kwargs):
    if "size" in kwargs:
        x1,y1 = kwargs["size"]
        screen.setup(x1,y1,0,0)
    s_size = (screen.window_width())*.95,(screen.window_height())*.97
    x,y = s_size[0]//2, s_size[1]//2
    return (x,y)

def color_method(**kwargs):
    if "gradient" in kwargs:
        color1,color2 = kwargs["gradient"]
        colors = gen_gradient(color1,color2)
    else:
        colors = gen_color_random()
    return colors

def setup(**kwargs):
    _keys = ["size","bgcolor","gradient","width","inc","speed","delay","tracer","colormode"]
    screen = gen_screen(**kwargs)
    width,height = screen_size(screen,**kwargs)
    colors = color_method(**kwargs)
    seq = get_visuals(width,height,screen,colors,**kwargs)
    return seq

def get_visuals(width,height,screen,colors,**kwargs):
    start,end,seq = -width,width,[]
    value,inc,gap,keys = get_defaults(**kwargs)
    while start < end:
        loc = Location((start,-height),len(seq))
        keys["color"] = next(colors)
        keys["value"] = value
        sect = Section.create(screen,**keys)
        loc.assign(sect)
        seq.append(loc)
        start += gap
        value += inc
    for loc in seq:
        loc.draw()
    return seq,screen

def get_defaults(**kwargs):
    _keys = {}
    _keys["speed"] = 0 if "speed" not in kwargs else kwargs["speed"]
    _keys["width"] = 7 if "width" not in kwargs else kwargs["width"]
    inc = 7 if "inc" not in kwargs else kwargs["inc"]
    gap = 10 if "gap" not in kwargs else kwargs["gap"]
    return inc,inc,gap,_keys


if __name__ == "__main__":
    kwargs = OPTIONS
    seq,screen = setup(**kwargs)
