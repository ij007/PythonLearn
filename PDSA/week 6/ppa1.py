def heapify(arr, n, i):
    minimum = i
    lc = (i*2)+1
    rc = (i*2)+2
    if lc<n and arr[lc]<arr[i]:
        minimum = lc
        
    if rc<n and arr[rc]<arr[i]:
        minimum = rc
        
    if i!=minimum:
        arr[i], arr[minimum] = arr[minimum], arr[i]
        heapify(arr, n, minimum)

def KminGreaterThan(arr, k, num):
    
    n = len(arr)
    for i in range(((n//2) - 1), -1, -1):
        heapify(arr, n, i)
        
    for i in range(n-1, n-k, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    if(arr[0] >= num):
        return True
        
    else:
        return False