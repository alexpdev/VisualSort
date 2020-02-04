# -*- encoding utf8-*-
from turtleSort.prep import setup
from turtleSort.funcs import shuffle,timer

@timer
def mergesort(seq):
    pos = [i.carbon_copy() for i in seq]
    _mergesort(seq)

def _mergesort(seq):
    if len(seq) <= 1: return seq
    left,right = seq[:len(seq)//2],seq[len(seq)//2:]
    left = _mergesort(left)
    right = _mergesort(right)
    i = j = k = 0
    temp = []
    while i < len(left) and j < len(right):
        if left[i].value < right[j].value:
            loc = duplic(left[i],seq[k])
            temp.append(loc)
            temp[-1].draw()
            i += 1
        else:
            loc = duplic(right[j],seq[k])
            temp.append(loc)
            temp[-1].draw()
            j += 1
        k += 1
    while i < len(left):
        loc = duplic(left[i],seq[k])
        temp.append(loc)
        temp[-1].draw()
        i += 1
        k += 1
    while j < len(right):
        loc = duplic(right[j],seq[k])
        temp.append(loc)
        temp[-1].draw()
        j += 1
        k += 1
    return temp

def duplic(copy,seqa):
    copy.remove()
    seqa.remove()
    loc = seqa.carbon_copy()
    sec = copy.sect.carbon_copy()
    loc.assign(sec)
    return loc

if __name__ == "__main__":
    seq,screen = setup()
    # shuffle(seq)
    mergesort(seq)
    screen.mainloop()
