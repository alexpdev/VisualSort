# -*- encoding utf8-*-
from ..utils.prep import setup
from ..utils.funcs import swap, shuffle

def mergesort(lst):
    l = len(lst)
    if l <= 1: return
    left,right = split_list(lst,l//2)
    mergesort(left)
    mergesort(right)
    i = j = k = 0
    while j < len(left) and k < len(right):
        if left[j].value < right[k].value:
            swap(lst[i],left[j])
            j += 1
        else:
            swap(lst[i],right[k])
            k += 1
        i += 1
    while j < len(left):
        swap(lst[i],left[j])
        j += 1
        i += 1
    while k < len(right):
        swap(lst[i],right[k])
        k += 1
        i += 1

def switch(a,b):
    a.remove()
    b.remove()
    c = b.sect
    b.sect = None
    a.assign(c)
    a.draw()

def split_list(lst,half):
    left,right = [],[]
    for i in lst[:half]:
        i.remove()
        copy = i.carbon_copy()
        left.append(copy)
        copy.draw()
    for i in lst[half:]:
        i.remove()
        copy = i.carbon_copy()
        right.append(copy)
        copy.draw()
    return left,right

if __name__ == "__main__":
    seq,screen = setup()
    shuffle(seq)
    mergesort(seq)
    screen.mainloop()
