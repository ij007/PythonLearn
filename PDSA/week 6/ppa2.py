def heapify(arr, n, i):
    
    largest = i
    lc = (i*2)+1
    rc = (i*2)+2
    
    if(lc<n and arr[lc]>arr[largest]):
        largest = lc
    if(rc<n and arr[rc]>arr[largest]):
        largest = rc
        
    if(largest != i):
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, n, largest)
def heapSort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

L = [int(item) for item in input().split(" ")]
heapSort(L)
print(*L)