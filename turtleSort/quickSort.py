# -*- coding utf8-*-
from turtleSort.prep import setup
from turtleSort.funcs import swap, shuffle, switch, timer

@timer
def quicksort(lst):
    _quicksort(lst,0,len(lst)-1)

def _quicksort(lst,lo,hi):
    if lo < hi:
        p = partition(lst,lo,hi)
        _quicksort(lst,lo,p-1)
        _quicksort(lst,p+1,hi)

def partition(arr,lo,hi):
    i,piv = lo - 1, arr[hi]
    for j in range(lo,hi):
        if arr[j].value < piv.value:
            i += 1
            if i != j:
                swap(arr[i],arr[j])
    swap(arr[i+1],arr[hi])
    return i+1

if __name__ == "__main__":
    seq,screen = setup()
    shuffle(seq)
    quicksort(seq)
    screen.mainloop()

    # left,right = 0,len(lst)
    # if right <= 1: return
    # pivot = int(right//2)
    # while left <= right:
    #     while lst[left].value < lst[pivot].value:
    #         left += 1
    #     while lst[right].value > lst[pivot].value:
    #         right += 1
    #     if left <= right:
    #         swap(lst[left],lst[right])
    #         left += 1
    #         right -= 1
