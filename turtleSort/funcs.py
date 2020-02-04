# -*- encoding utf8-*-
# turtleSort.sorts.funcs
import random
from time import time

def swap(loca,locb,shuffle=False):
    """ Utility for swapping one of a list's Section item with another in place.
        In: Location objects that contain the Sects for swapping (qty=2) Out: None """
    loca.remove(shuffle)
    locb.remove(shuffle)
    seca = loca.sect
    loca.assign(locb.sect)
    locb.assign(seca)
    loca.draw(shuffle)
    locb.draw(shuffle)
    return


def shuffle(lst):
    """ Randomly shuffles sequence of colored Sections in place
        In: full array of drawn location objects. Out: None """
    ints = list(range(len(lst)))
    for z in range(1,len(lst)):
        ints.remove(z-1)
        ints.remove(z)
        num = random.choice(ints)
        ints.remove(num)
        num2 = random.choice(ints)
        swap(lst[z],lst[num],True)
        swap(lst[z-1],lst[num2],True)
        ints += [z-1,z,num]
    lst[0].sect.screen.update()
    return


def switch(a,b):
    """ Function for swaping current Section object for another. Uses a copy
        In: Location objects.  Out: None """
    a.remove()
    b.remove()
    c = b.sect
    b.sect = None
    a.assign(c)
    a.draw()

def timer(func):
    def wrapper(seq):
        shuffle(seq)
        then = time()
        func(seq)
        now = time()
        print("time: ",now-then)
    return wrapper
