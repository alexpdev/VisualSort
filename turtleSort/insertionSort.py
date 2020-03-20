# -*- encoding utf8-*-
from turtleSort.prep import setup
from turtleSort.funcs import swap, shuffle,timer


@timer
def insertionsort(lst):
    for i in range(1,len(lst)):
        j,k = i,i-1
        while j > 0 and lst[k].value > lst[j].value:
            swap(lst[j],lst[k])
            j -= 1
            k -= 1
    return

