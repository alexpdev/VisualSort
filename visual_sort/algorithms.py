from visual_sort.utils import timer

@timer
def InsertionSort(stage):
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
def SelectionSort(stage):
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
def BubbleSort(stage):
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
def CocktailSort(stage):
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
def QuickSort(stage):
    lo = 0
    hi = len(stage) - 1
    return _quicksort(stage, lo, hi)


def partition(stage, lo, hi):
    pivot = lo
    for i in range(lo+1, hi+1):
        if stage[i] <= stage[lo]:
            pivot += 1
            stage[i], stage[pivot] = stage[pivot], stage[i]
    stage[pivot], stage[lo] = stage[lo], stage[pivot]
    return pivot


def _quicksort(stage, lo, hi):
    if lo >= hi:
        return
    pivot = partition(stage, lo, hi)
    _quicksort(stage, lo, pivot-1)
    _quicksort(stage, pivot+1, hi)


@timer
def StoogeSort(stage):
    _stoogesort(stage, 0, len(stage)-1)


def _stoogesort(stage, lo, hi):
    if stage[lo] > stage[hi]:
        block = stage[lo]
        stage[lo] = stage[hi]
        stage[hi] = block
    diff = hi - lo + 1
    if diff > 2:
        m = int(diff/3)
        _stoogesort(stage, lo, hi - m)
        _stoogesort(stage, lo + m, hi)
        _stoogesort(stage, lo, hi - m)
    return


def flip(stage, k):
    left = 0
    while left < k:
        block = stage[left]
        stage[left] = stage[k]
        stage[k] = block
        k -= 1
        left += 1

def max_index(stage, k):
    index = 0
    for i in range(k):
        if stage[i] > stage[index]:
            index = i
    return index

@timer
def PancakeSort(stage):
    n = len(stage)
    while n > 1:
        maxdex = max_index(stage, n)
        flip(stage, maxdex)
        flip(stage, n - 1)
        n -= 1


@timer
def OddEvenSort(stage):
    complete = False
    while not complete:
        complete = True
        for i in range(1, len(stage) - 1, 2):
            if stage[i] > stage[i + 1]:
                block = stage[i]
                stage[i] = stage[i+1]
                stage[i+1] = block
                complete = False
        for i in range(0, len(stage) - 1, 2):
            if stage[i] > stage[i + 1]:
                block = stage[i]
                stage[i] = stage[i+1]
                stage[i+1] = block
                complete = False


def is_sorted(stage):
    for i in range(1,len(stage)):
        if stage[i] < stage[i-1]:
            return False
    return True

@timer
def MergeSort(stage):
    seq, vals = [], []
    for i, block in enumerate(stage):
        vals.append(block.height)
        seq.append((block,i))
    _mergesort(stage, seq, vals)


def _mergesort(stage, seq, vals):
    if len(seq) <= 1: return
    mid = len(seq) // 2
    left_seq = seq[:mid]
    right_seq = seq[mid:]
    left_vals = vals[:mid]
    right_vals = vals[mid:]
    _mergesort(stage, left_seq, left_vals)
    _mergesort(stage, right_seq, right_vals)
    i = j = k = 0
    while i < len(left_seq) and j < len(right_seq):
        if left_vals[i] < right_vals[j]:
            block, _ = left_seq[i]
            stage[seq[k][1]] = block
            seq[k] = left_seq[i]
            vals[k] = left_vals[i]
            i += 1
        else:
            block, _ = right_seq[j]
            stage[seq[k][1]] = block
            seq[k] = right_seq[j]
            vals[k] = right_vals[j]
            j += 1
        k += 1
    while i < len(left_seq):
        block, _ = left_seq[i]
        stage[seq[k][1]] = block
        seq[k] = left_seq[i]
        vals[k] = left_vals[i]
        i += 1
        k += 1
    while j < len(right_seq):
        block, _ = right_seq[j]
        stage[seq[k][1]] = block
        seq[k] = right_seq[j]
        vals[k] = right_vals[j]
        j += 1
        k += 1

@timer
def GnomeSort(stage):
    _gnomesort(stage, len(stage))

def _gnomesort(stage, size):
    i = 0
    while i < size:
        if i == 0:
            i += 1
        if stage[i] >= stage[i - 1]:
            i += 1
        else:
            block = stage[i]
            stage[i] = stage[i - 1]
            stage[i - 1] = block
            i -= 1


@timer
def ShellSort(stage):
    size = len(stage)
    mid = size // 2
    while mid > 0:
        for idx in range(mid, size):
            block = stage[idx]
            pos = idx
            while  pos >= mid and stage[pos - mid] > block:
                stage[pos] = stage[pos - mid]
                pos -= mid
            stage[pos] = block
        mid = mid // 2


def _sort(stage, start, end):
    for i in range(start + 1, end + 1):
        j = i
        while j > start and stage[j] < stage[j - 1]:
            block = stage[j]
            stage[j] = stage[j - 1]
            stage[j - 1] = block
            j -= 1


def _merge(stage, lo, mid, hi):
    len1, len2 = mid - lo + 1, hi - mid
    left, right = [], []
    for i in range(len1):
        left.append(stage[lo + i])
    for i in range(len2):
        right.append(stage[mid + 1 + i])
    i = j = k = 0
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            stage[k] = left[i]
            i += 1
        else:
            stage[k] = right[j]
            j += 1
        k += 1
    while i < len1:
        stage[k] = left[i]
        i += 1
        k += 1
    while j < len2:
        stage[k] = right[j]
        j += 1
        k += 1

@timer
def TimSort(stage):
    size = len(stage)
    gap = size // 2
    for start in range(0, size, gap):
        end = min(start + gap - 1, size - 1)
        _sort(stage, start, end)
    run = gap
    while run < size:
        for lo in range(0, size, 2 * run):
            mid = min(size - 1, lo + run - 1)
            hi = min((lo + 2 * run - 1),(size - 1))
            if mid < hi:
                _merge(stage, lo, mid, hi)
        run *= 2


def getNextGap(gap):
    gap = (gap * 10)//13
    if gap < 1:
        return 1
    return gap

@timer
def CombSort(arr):
    n = len(arr)
    gap = n
    swapped = True
    while gap !=1 or swapped == 1:
        gap = getNextGap(gap)
        swapped = False
        for i in range(0, n-gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap]=arr[i + gap], arr[i]
                swapped = True
