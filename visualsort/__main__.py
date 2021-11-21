import logging
import sys
from visualsort.utils import get_screen
from visualsort.objects import Stage
from visualsort.algorithms import (
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

class Runner:
    def __init__(self, stage):
        self.stage = stage

    def run(self, x=None, y=None):
        OddEvenSort(self.stage)
        BubbleSort(self.stage)
        CombSort(self.stage)
        StoogeSort(self.stage)
        PancakeSort(self.stage)
        InsertionSort(self.stage)
        SelectionSort(self.stage)
        CocktailSort(self.stage)
        GnomeSort(self.stage)
        ShellSort(self.stage)
        QuickSort(self.stage)
        MergeSort(self.stage)
        TimSort(self.stage)
        self.stage.screen.update()



def main(args=None):
    if args: print(args)
    logger.debug(f"command line args {args}")
    screen = get_screen()
    stage = Stage.create(screen)
    runner = Runner(stage)
    stage.screen.onclick(runner.run, btn=1, add=True)
    screen.listen()
    stage.screen.mainloop()


if __name__ == "__main__":
    main(sys.argv[1:])