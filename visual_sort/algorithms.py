from visual_sort.utils import timer


@timer
def insertionsort(stage):
    for idx in range(1,len(stage)):
        current = stage[idx]
        j = idx - 1
        if stage[j] > current:
            while j >= 0 and stage[j] > current:
                item = stage[j]
                stage[j+1] = item
                j -= 1
            stage[j+1] = current

@timer
def selectionsort(stage):
    for i in range(len(stage)-1):
        mindex = i
        smallest = stage[mindex]
        for j in range(i+1, len(stage)):
            if stage[j] < stage[mindex]:
                mindex = j
                smallest = stage[mindex]
        while mindex > i:
            item = stage[mindex-1]
            stage[mindex] = item
            mindex -= 1
        stage[i] = smallest


@timer
def bubblesort(stage):
    while True:
        swaps = 0
        for i in range(1,len(stage)):
            bar1 = stage[i-1]
            bar2 = stage[i]
            if bar1 > bar2:
                stage[i-1] = bar2
                stage[i] = bar1
                swaps += 1
        if swaps == 0:
            return

@timer
def shellsort(stage):
    while True:
        swaps = 0
        for i in range(1,len(stage)):
            block1 = stage[i-1]
            block2 = stage[i]
            if block1 > block2:
                stage[i-1] = block2
                stage[i] = block1
                swaps += 1
        if swaps == 0: break
        swaps = 0
        while i > 0:
            block1 = stage[i-1]
            block2 = stage[i]
            if block2 < block1:
                stage[i-1] = block2
                stage[i] = block1
                swaps += 1
            i -= 1
        if swaps == 0: break




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
        stage[pos] = item2
        stage[count] = item1
        pos = count
        swaps += 1

@timer
def quicksort(stage):
    hi = len(stage) - 1
    _quicksort(stage, 0, hi)

def partition(stage, lo, hi):
    pivot = lo
    for i in range(lo+1, hi+1):
        if stage[i] <= stage[lo]:
            pivot += 1
            stage[i], stage[pivot] = stage[pivot], stage[i]
    stage[pivot], stage[lo] = stage[lo], stage[pivot]
    return pivot

def _quicksort(stage, lo=0, hi=None):
    if hi is None:
        hi = len(stage) - 1
    def __quickysort(stage, lo, hi):
        if lo >= hi:
            return
        pivot = partition(stage, lo, hi)
        __quickysort(stage, lo, pivot-1)
        __quickysort(stage, pivot+1, hi)
    return __quickysort(stage, lo, hi)

@timer
def mergesort(stage):
    _mergesort(stage)


def _mergesort(stage):
    if len(stage) > 1:
        mid = len(stage) // 2
        left = stage[:mid]
        right = stage[mid:]
        left = _mergesort(left)
        right = _mergesort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              stage[k] = left[i]
              i += 1
            else:
                stage[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            stage[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            stage[k]=right[j]
            j += 1
            k += 1
    return stage
