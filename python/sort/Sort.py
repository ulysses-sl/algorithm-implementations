def bubble_sort(arr):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(1, len(arr)):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
                is_sorted = False


def selection_sort(arr):
    for i in range(len(arr)):
        minimum = arr[i]
        minimum_idx = i
        for j in range(i, len(arr)):
            if arr[j] < minimum:
                minimum = arr[j]
                minimum_idx = j
        arr[i], arr[minimum_idx] = arr[minimum_idx], arr[i]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            temp = arr[i]
            j = i
            while j > 0 and arr[j-1] > temp:
                arr[j] = arr[j-1]
                j -= 1
            arr[j] = temp


def quicksort(arr):
    qst(arr, 0, len(arr)-1)


def find_pivot(arr, i, j):
    m = i + (j - i) // 2
    if arr[i] >= arr[m]:
        if arr[m] >= arr[j]:
            p = m
        elif arr[i] >= arr[j]:
            p = j
        else:
            p = i
    else:  # arr[i] < arr[m]
        if arr[m] <= arr[j]:
            p = m
        elif arr[i] <= arr[j]:
            p = j
        else:
            p = i
    return p


def qst(arr, i, j):
    if i >= j:
        return
    p = find_pivot(arr, i, j)
    pv = arr[p]
    x = i
    xx = p-1
    y = p+1
    yy = j


