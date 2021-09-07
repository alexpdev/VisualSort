#! env/Scripts/python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from visual_sort.conf import OPTIONS
from visual_sort.classes import Window, Bar, Stage
from visual_sort.sorting import ( bubblesort, cyclesort, selectionsort,
                                  insertionsort, mergesort, quicksort )


def setup():
    pass

__all__ = [Window, Bar, Stage, setup, OPTIONS]

def setup(**kwargs):
    print(kwargs)
    def main(x,y):
        window.stage.shuff_x(1)
        window.title.write("Bubble Sort", align="center", move=False, font=("Arial",26,"bold"))
        bubblesort(window.stage)
        window.title.clear()
        window.stage.shuff_x(1)
        window.title.write("Cycle Sort", align="center", move=False, font=("Arial",26,"bold"))
        cyclesort(window.stage)
        window.title.clear()
        window.stage.shuff_x(1)
        window.title.write("Selection Sort", align="center", move=False, font=("Arial",26,"bold"))
        selectionsort(window.stage)
        window.title.clear()
        window.stage.shuff_x(1)
        window.title.write("Insertion Sort", align="center", move=False, font=("Arial",26,"bold"))
        insertionsort(window.stage)
        window.title.clear()
        window.stage.shuff_x(1)
        window.title.write("Merge Sort", align="center", move=False, font=("Arial",26,"bold"))
        mergesort(window.stage)
        window.title.clear()
        window.stage.shuff_x(1)
        window.title.write("Quick Sort", align="center", move=False, font=("Arial",26,"bold"))
        quicksort(window.stage)
        window.title.clear()
    window = Window(**kwargs)
    window.screen.onscreenclick(main,1,False)
    return window


if __name__ == "__main__":
    window = setup(**OPTIONS)
    window.screen.mainloop()
