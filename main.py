from visual_sort.classes import Stage
from visual_sort.sorting import insertionsort, selectionsort, bubblesort, quicksort, mergesort, cyclesort
from visual_sort.utils import get_screen


if __name__ == '__main__':
    screen = get_screen()
    stage = Stage.create(screen)
    cyclesort(stage)
    # insertionsort(stage)
    selectionsort(stage)
    # bubblesort(stage)
    quicksort(stage)
    mergesort(stage)
