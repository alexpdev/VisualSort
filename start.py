from visual_sort import conf
from visual_sort.utils import get_screen
from visual_sort.objects import Stage
from visual_sort.algorithms import selectionsort, insertionsort, bubblesort, cyclesort, quicksort, mergesort, shellsort


if __name__ == '__main__':
    screen = get_screen()
    stage = Stage.create(screen)
    bubblesort(stage)
    shellsort(stage)
    insertionsort(stage)
    selectionsort(stage)
    cyclesort(stage)
    quicksort(stage)
    mergesort(stage)

