from visual_sort.utils import timer


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
    if len(stage) == 1:
        return stage
    if lo < hi:
        pivot = partition(stage,lo,hi)
        _quicksort(stage,lo,pivot-1)
        _quicksort(stage,pivot+1,hi)

def partition(stage,lo,hi):
    pivot = stage[hi]
    index = lo
    for j in range(lo,hi):
        if stage[j] <= pivot:
            block1 = stage[index]
            block2 = stage[j]
            stage[j] = block2
            stage[index] = block1
            index = index + 1
    stage[hi] = stage[index]
    stage[index] = pivot
    return index



def mergesort(stage):
    blocks = [block for block in stage]
    idxs = [i for i in range(len(stage))]
    return _mergesort(blocks, idxs, stage)

@timer
def _mergesort(blocks, idxs, stage):
    length = len(blocks) // 2
    if len(stage1) <= 1:
        return stage1
    l = stage1[:length]
    r = stage1[length:]
    print(l)
    print(r)
    left = mergesort(l)
    right = mergesort(r)
    i = j = k = 0
    while i < len(left) and k < len(right):
        if left[i] < right[k]:
            stage[k] = left[i]
            i += 1
        else:
            stage[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        stage[k] = left[i]
        i += 1
        k +=  1
    while j < len(right):
        stage[k] = right[j]
        j += 1
        k += 1
    return stage
