# -*- encoding utf8-*-
from visuals.utils.prep import setup
from visuals.utils.funcs import swap, shuffle

def bubblesort1(lst):
    l,z = len(lst),1
    while True:
        for i in range(l):
            while i+1 < l and lst[i].value > lst[i+1].value:
                swap(lst[i],lst[i+1])
                i += 1

def bubblesort(lst):
    counter,l,z,t = 1,len(lst),0,1
    while counter:
        counter = 0
        for i,x in enumerate(lst):
            if i+1 < l and x.value > lst[i+1].value:
                counter += 1
                swap(x,lst[i+1])
                print(counter)


if __name__ == "__main__":
    seq,screen = setup()
    shuffle(seq)
    bubblesort(seq)
    screen.mainloop()
