# -*- encoding utf8-*-
from visuals.utils.prep import setup
from visuals.utils.funcs import swap, shuffle

def selection_sort(lst):
    l,z = len(lst),0
    while z < l:
        sml = z
        for i in range(z,len(lst)):
            if lst[i].value < lst[sml].value:
                sml = i
        swap(lst[z],lst[sml])
        z += 1
    return



if __name__ == "__main__":
    seq,screen = setup()
    shuffle(seq)
    selection_sort(seq)
    screen.mainloop()
