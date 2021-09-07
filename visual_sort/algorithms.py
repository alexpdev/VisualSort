import random
from time import time

def timer(func):
    def wrapper(stage):
        stage = stage
        shuffle(stage)
        shuffle(stage)
        then = time()
        func(stage)
        print(f"{func.__name__} Duration: {time() - then} seconds.")
        return stage
    return wrapper

def shuffle(stage):
    l = list(range(len(stage)))
    for _ in range(200):
        r1 = random.choice(l)
        l.remove(r1)
        r2 = random.choice(l)
        l.append(r1)
        current1 = stage[r1]
        current2 = stage[r2]
        del stage[r1]
        del stage[r2]
        stage[r1] = current2
        stage[r2] = current1

@timer
def insertionsort(stage):
    for idx in range(1,len(stage)):
        j = idx - 1
        if stage[j] <= stage[idx]: continue
        cur = stage[idx]
        del stage[idx]
        while j >= 0 and stage[j] > cur:
            item = stage[j]
            del stage[j]
            stage[j+1] = item
            j -= 1
        stage[j+1] = cur

@timer
def selectionsort(stage):
    for i in range(len(stage)-1):
        item1 = stage[i]
        minindex = i
        for j in range(i+1, len(stage)):
            if stage[j] < stage[minindex]:
                minindex = j
        if item1 != stage[minindex]:
            minimum = stage[minindex]
            del stage[i]
            del stage[minindex]
            stage[i] = minimum
            stage[minindex] = item1

@timer
def bubblesort(stage):
    while True:
        swaps = 0
        for i in range(1,len(stage)):
            bar1 = stage[i-1]
            bar2 = stage[i]
            if bar1 > bar2:
                del stage[i-1]
                del stage[i]
                stage[i-1] = bar2
                stage[i] = bar1
                swaps += 1
        if swaps == 0:
            return

@timer
def cyclesort(stage):
    swaps = pos = 0
    while True:
        count = 0
        if pos == len(stage):
            if swaps == 0:
                return
            swaps = pos = 0
        for i in range(len(stage)):
            if stage[i] < stage[pos]:
                count += 1
        if pos == count:
            pos += 1
            continue
        item1 = stage[pos]
        item2 = stage[count]
        del stage[pos]
        del stage[count]
        stage[pos] = item2
        stage[count] = item1
        pos = count
        swaps += 1

@timer
def quicksort(stage):
    hi = len(stage) - 1
    _quicksort(stage,0,hi)

def _quicksort(stage,lo,hi):
    if lo < hi:
        pivot = partition(stage,lo,hi)
        _quicksort(stage,lo,pivot-1)
        _quicksort(stage,pivot+1,hi)

def partition(stage,lo,hi):
    index = lo - 1
    for j in range(lo+1,hi):
        if stage[j] < stage[hi]:
            index += 1
            print(j)
            print(index)
            item1 = stage[j]
            item2 = stage[index]
            del stage[j]
            del stage[index]
            stage[j] = item2
            stage[index] = item1
    item1 = stage[hi]
    item2 = stage[index+1]
    del stage[hi]
    del stage[index + 1]
    stage[hi] = item2
    stage[index + 1] = item1
    return index + 1


@timer
def mergesort(stage):
    arr = list(range(len(stage)))
    _mergesort(stage, arr)

def _mergesort(stage, arr):
    if len(stage) <= 1: return stage
    L = [stage[i] for i in range(len(stage)//2)]
    R= [stage[j] for j in range(len(stage)//2,len(stage))]
    left = _mergesort(stage, L)
    right = _mergesort(stage, R)
    arr = []
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1
        k += 1
    while i < len(left):
        arr.append(left[i])
        i += 1
        k += 1
    while j < len(right):
        arr.append(right[j])
        j += 1
        k += 1
    for idx, block1 in enumerate(left + right):
        block1 = block1
        block2 = arr[idx]
        if block1 == block2: continue
        stage_index1 = block1.index()
        stage_index2 = block2.index()
        del stage[stage_index1]
        del stage[stage_index2]
        stage[stage_index1] = block2
        stage[stage_index2] = block1
    return arr


