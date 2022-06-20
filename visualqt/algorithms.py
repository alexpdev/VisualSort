def bubblesort(rects):
    while True:
        swaps = 0
        for i in range(1,len(rects)):
            if rects[i-1] > rects[i]:
                rects.swap(i-1, i)
                swaps += 1
        if swaps == 0:
            return
