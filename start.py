from visual_sort import conf
from visual_sort.utils import get_screen
from visual_sort.objects import Stage
from visual_sort.algorithms import selectionsort, insertionsort, bubblesort, cyclesort, quicksort, mergesort


if __name__ == '__main__':
    args = [conf.SCREEN_SIZE, conf.BACKGROUND, conf.TRACER, conf.DELAY]
    screen = get_screen()
    stage = Stage.create(screen)
    insertionsort(stage)
    selectionsort(stage)
    bubblesort(stage)
    cyclesort(stage)
    quicksort(stage)
    mergesort(stage)
    stage.clear()

