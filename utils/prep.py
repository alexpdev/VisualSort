# -*- encoding utf8-*-
# turtleSort.utils.prep
from turtleSort.utils.classes import Location,Section
from turtle import Screen
import random

def gen_color():
    nums = list(range(1,255,10))
    colors = [random.choice(nums) for i in range(3)]
    return tuple(colors)

def gen_screen():
    screen = Screen()
    screen.colormode(255)
    screen.tracer(1,0)
    return screen

def screen_size(screen,size=None):
    if size:
        screen.setup(size[0],size[1],0,0)
    s_size = (screen.window_width())*.9,(screen.window_height())*.95
    x,y = s_size[0]//2, s_size[1]//2
    return (x,y)

def setup():
    screen = gen_screen()
    width,height = screen_size(screen)
    lst,start,end,value = [],-width,width,8
    while start < end:
        xy = (start,-height)
        loc = Location(xy,len(lst))
        color = gen_color()
        kwargs = {"speed":0,"color":color,"value":value,"width":7}
        sect = Section.create(screen,**kwargs)
        loc.assign(sect)
        lst.append(loc)
        start += 10
        value += 7
    for loc in lst:
        loc.draw()
    return lst,screen

if __name__ == "__main__":
    setup()
