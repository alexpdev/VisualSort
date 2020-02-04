from prep import setup
from config import OPTIONS as kwargs
from bubbleSort import bubblesort
from quickSort import quicksort
from insertionSort import insertionsort
from selectionSort import selectionsort
from mergeSort import mergesort
from cycleSort import cyclesort
from funcs import timer, shuffle

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
