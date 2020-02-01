# -*- encoding utf8-*-
from turtleSort.utils.prep import setup
from turtleSort.utils.funcs import swap, shuffle

def insertionsort(lst):
    for i in range(1,len(lst)):
        j,k = i,i-1
        while j > 0 and lst[k].value > lst[j].value:
            swap(lst[j],lst[k])
            j -= 1
            k -= 1
    return


if __name__ == "__main__":
    seq,screen = setup()
    shuffle(seq)
    insertion_sort(seq)
    screen.mainloop()
