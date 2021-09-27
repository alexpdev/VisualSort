import logging
import sys
from visual_sort.utils import get_screen
from visual_sort.objects import Stage
from visual_sort.algorithms import (
    SelectionSort,
    InsertionSort,
    BubbleSort,
    QuickSort,
    ShellSort,
    StoogeSort,
    PancakeSort,
    OddEvenSort,
    MergeSort,
    CocktailSort,
    ShellSort,
    TimSort,
    GnomeSort,
    CombSort
    )

"""Visual Sorting Implementations."""

__version__ = "1.1"

logger = logging.getLogger(__name__)

def run(stage):
    OddEvenSort(stage)
    BubbleSort(stage)
    CombSort(stage)
    StoogeSort(stage)
    PancakeSort(stage)
    InsertionSort(stage)
    SelectionSort(stage)
    CocktailSort(stage)
    GnomeSort(stage)
    ShellSort(stage)
    QuickSort(stage)
    MergeSort(stage)
    TimSort(stage)


def main(args=None):
    if args: print(args)
    logger.debug(f"command line args {args}")
    screen = get_screen()
    stage = Stage.create(screen)
    run(stage)
    stage.screen.onkey(lambda: run(stage), "Up")
    stage.screen.mainloop()


if __name__ == "__main__":
    main(sys.argv[1:])
