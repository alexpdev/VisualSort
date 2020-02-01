# -*- encoding utf8-*-
# visual_sorting.utils.funcs
import random

def swap(loca,locb):
    """ Utility for swapping one of a list's Section item with another in place.
        In: Location objects that contain the Sects for swapping (qty=2) Out: None """
    loca.remove()
    locb.remove()
    seca = loca.sect
    loca.assign(locb.sect)
    locb.assign(seca)
    loca.draw()
    locb.draw()
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
        swap(lst[x],lst[num])
        swap(lst[z-1],lst[num2])
        ints += [z-1,z,num]
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
