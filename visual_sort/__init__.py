#! /usr/bin/python3
# -*- coding: utf-8 -*-

import logging
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

def main(args=None):
    if args: print(args)
    logger.debug(f"command line args {args}")
    screen = get_screen()
    stage = Stage.create(screen)
    print(len(stage))
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
