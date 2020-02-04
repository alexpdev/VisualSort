# -*- encoding utf8-*-
from prep import setup
from funcs import swap, shuffle, timer

@timer
def selectionsort(lst):
    for i in range(len(lst)):
        current = i
        for j in range(i,len(lst)):
            if lst[j].value < lst[current].value:
                current = j
        swap(lst[i],lst[current])
    return




if __name__ == "__main__":
    seq,screen = setup()
    shuffle(seq)
    selectionsort(seq)
    screen.mainloop()
