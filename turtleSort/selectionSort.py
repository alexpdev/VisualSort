# -*- coding utf8-*-
from turtleSort.prep import setup
from turtleSort.funcs import swap, shuffle, timer

@timer
def selectionsort(lst):
    for i in range(len(lst)):
        current = i
        for j in range(i,len(lst)):
            if lst[j].value < lst[current].value:
                current = j
        swap(lst[i],lst[current])
    return

