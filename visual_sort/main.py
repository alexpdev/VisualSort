import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from visual_sort.config import OPTIONS
from visual_sort.classes import Window, Bar, Stage
from visual_sort.sorting import ( bubblesort, cyclesort, selectionsort,
                                  insertionsort, mergesort, quicksort )

def setup(**kwargs):
    window = Window(**kwargs)
    window.stage.shuff_x(2)
    bubblesort(window.stage)
    window.stage.shuff_x(2)
    cyclesort(window.stage)
    window.stage.shuff_x(2)
    selectionsort(window.stage)
    window.stage.shuff_x(2)
    insertionsort(window.stage)
    window.stage.shuff_x(2)
    mergesort(window.stage)
    window.stage.shuff_x(2)
    quicksort(window.stage)
    window.screen.mainloop()


if __name__ == "__main__":
    setup(**OPTIONS)
