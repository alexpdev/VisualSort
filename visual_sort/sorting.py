from time import time

def timer(func):
    def wrapper(*args,**kwargs):
        then = time()
        func(*args,**kwargs)
        now = time()
        print("time: ",now-then)
    return wrapper

@timer
def bubblesort(stage):
    while True:
        swaps = 0
        for i in range(1,len(stage)):
            bar1 = stage.vals[i-1]
            bar2 = stage.vals[i]
            if bar1.value > bar2.value:
                stage.swap(i-1,i)
                bar1.remove()
                bar1.draw()
                bar2.remove()
                bar2.draw()
                swaps += 1
        if swaps == 0:
            return

@timer
def cyclesort(stage):
    _cyclesort(stage,0)

def _cyclesort(stage,pos):
    if pos == len(stage): return
    barval,counter = stage.vals[pos].value,0
    for bar in stage.vals:
        counter = counter + 1 if bar.value > barval else counter
    p = len(stage) - counter - 1
    if pos == p:
        return _cyclesort(stage,pos+1)
    else:
        bar1,bar2 = stage.swap(pos,p)
        stage.redraw(bar1,bar2)
        return _cyclesort(stage,pos)

@timer
def selectionsort(stage):
    new_vals = []
    for i in range(len(stage)):
        pos,sml = i,stage.vals[i].value
        for j in range(i,len(stage)):
            jval = stage.vals[j].value
            if jval < sml:
                pos,sml = j,jval
        while pos > i:
            bar1,bar2 = stage.swap(pos,pos-1)
            stage.redraw(bar1,bar2)
            pos -= 1
    return

@timer
def insertionsort(stage):
    for i in range(len(stage)):
        bar,pos = stage.vals[i],i
        while pos > 0:
            if bar.value < stage.vals[pos-1].value:
                bar1,bar2 = stage.swap(pos,pos-1)
                stage.redraw(bar1,bar2)
            pos -= 1
    return

@timer
def mergesort(stage):
    _mergesort(stage.vals)

def _mergesort(vals):
    if len(vals) <= 1: return vals
    half = len(vals)//2
    left,right = vals[:half],vals[half:]
    _mergesort(left)
    _mergesort(right)
    left,right = tuple(left),tuple(right)
    l=r=k=0
    while l < len(left) and r < len(right):
        if left[l].value < right[r].value:
            merge_switch(vals,k,left[l])
            l += 1
        else:
            merge_switch(vals,k,right[r])
            r += 1
        k += 1
    while l < len(left):
        merge_switch(vals,k,left[l])
        l += 1
        k += 1
    while r < len(right):
        merge_switch(vals,k,right[r])
        r += 1
        k += 1
    return vals

def merge_switch(arr,i,item):
    idx = arr[i].idx
    arr[i].remove()
    item1 = arr[i]
    del item1
    item.remove()
    arr[i] = item.copy()
    arr[i].setposition(idx)
    arr[i].draw()
    return

@timer
def quicksort(stage):
    hi = len(stage.vals) - 1
    _quicksort(stage.vals,0,hi)

def _quicksort(vals,lo,hi):
    if lo < hi:
        p = partition(vals,lo,hi)
        _quicksort(vals,lo,p-1)
        _quicksort(vals,p+1,hi)

def partition(arr,lo,hi):
    i,piv = lo - 1, arr[hi]
    for j in range(lo,hi):
        if arr[j].value < piv.value:
            i += 1
            if i != j:
                b1,b2 = piv.stage.swap(arr[i].idx,arr[j].idx)
                piv.stage.redraw(b1,b2)
    b1,b2 = piv.stage.swap(arr[i+1].idx,arr[hi].idx)
    piv.stage.redraw(b1,b2)
    return i+1
