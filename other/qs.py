import random

def partition(arr,low,high):
    i = ( low-1 )         # index of smaller element
    pivot = arr[high]     # pivot
    for j in range(low , high):
        if   arr[j] < pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            print(arr)
    arr[i+1],arr[high] = arr[high],arr[i+1]
    print(arr)
    return ( i+1 )

def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def qs(lst):
    low = 0
    hi = len(lst) - 1
    quickSort(lst,low,hi)

a = list(range(100))
lst = []
for i in range(15):
    b = random.choice(a)
    a.remove(b)
    lst.append(b)
qs(lst)
