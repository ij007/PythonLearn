def findLargest(L):
    (start,end) = (0, len(L))
    (left, right) = (L[0], L[-1])
    
    while(start<end):
        
        mid = (start+end)//2
        if(left>L[mid]):
            end = mid
        else:
            start = mid+1
    return L[start-1]