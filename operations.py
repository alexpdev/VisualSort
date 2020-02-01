import random

def swap(loca,locb):
    loca.remove()
    locb.remove()
    seca = loca.sect
    loca.assign(locb.sect)
    locb.assign(seca)
    loca.draw()
    locb.draw()
    return True

def shuffle(lst):
    l = len(lst)
    ints = list(range(0,l))
    for z in range(l):
        ints.remove(z)
        num = random.choice(ints)
        loca,locb = lst[num],lst[z]
        swap(loca,locb)
        ints.append(z)
        z += 1
    return True

def switch(a,b):
    a.remove()
    b.remove()
    c = b.sect
    b.sect = None
    a.assign(c)
    a.draw()

def alternate(a,b):

    cpy = a.carbon_copy
