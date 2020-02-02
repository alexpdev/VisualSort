# -*- encoding utf8-*-
from ..utils.prep import setup
from ..utils.funcs import swap, shuffle

def cyclesort(lst):
    nums,last,val,fin = [i.value for i in lst],0,0,1
    while fin:
        dest = find_pos(lst[val],nums)
        if val != dest:
            swap(lst[dest],lst[val])
            val = dest
            fin += 1
        elif val+1 >= len(lst):
            fin = 1 if fin > 1 else 0
            val = 0
        else:
            val += 1

def first_out(lst):
    for i,x in enumerate(lst):
        if i > 0 and x.value < lst[i-1].value:
            return i-1

def find_pos(elem,nums):
    val = elem.value
    lst = [i for i in nums if i < val]
    return len(lst)


if __name__ == "__main__":
    seq,screen = setup()
    shuffle(seq)
    cyclesort(seq)
    screen.mainloop()
