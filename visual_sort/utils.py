import random as rand
from visual_sort import conf

def gen_color():
    chars = "123456789ABCDEF"
    return "#" + "".join([rand.choice(chars) for i in range(6)])


def screen_extend(screen):
    winHeight = screen.window_height()*.95
    winWidth = screen.window_width()*.95
    screen.halfh = winHeight / 2
    screen.halfw = winWidth / 2

