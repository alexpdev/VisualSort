import sys
from visual_sort.objects import Stage
from visual_sort.utils import get_screen
from visual_sort.algorithms import (insertionsort, selectionsort, quicksort,
                                    mergesort, cyclesort, bubblesort, shellsort)

def main(args):
    screen = get_screen()
    stage = Stage.create(screen)
    bubblesort(stage)
    shellsort(stage)
    insertionsort(stage)
    selectionsort(stage)
    cyclesort(stage)
    mergesort(stage)
    quicksort(stage)
    print(args)


if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)

