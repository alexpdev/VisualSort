from turtleSort.prep import setup
from turtleSort.config import OPTIONS as kwargs
from turtleSort.bubbleSort import bubblesort
from turtleSort.quickSort import quicksort
from turtleSort.insertionSort import insertionsort
from turtleSort.selectionSort import selectionsort
from turtleSort.mergeSort import mergesort
from turtleSort.cycleSort import cyclesort
from turtleSort.funcs import timer, shuffle

def main(seq):
    bubblesort(seq)
    insertionsort(seq)
    selectionsort(seq)
    seq = mergesort(seq)
    quicksort(seq)
    cyclesort(seq)

if __name__ == "__main__":
    kwargs["gradient"] = ((255,150,0),(100,0,255))
    kwargs["size"] = (.9,.9)
    seq,screen = setup(**kwargs)
    main(seq)
    screen.mainloop()
