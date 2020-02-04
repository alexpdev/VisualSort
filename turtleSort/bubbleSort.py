# -*- encoding utf8-*-
from turtleSort.prep import setup
from turtleSort.funcs import swap, shuffle, timer

def bubblesort1(lst):
    l,z = len(lst),1
    while True:
        for i in range(l):
            while i+1 < l and lst[i].value > lst[i+1].value:
                swap(lst[i],lst[i+1])
                i += 1

@timer
def bubblesort(lst):
    counter,l,z,t = 1,len(lst),0,1
    while counter:
        counter = 0
        for i,x in enumerate(lst):
            if i+1 < l and x.value > lst[i+1].value:
                counter += 1
                swap(x,lst[i+1])


if __name__ == "__main__":
    seq,screen = setup()
    shuffle(seq)
    bubblesort(seq)
    screen.mainloop()
