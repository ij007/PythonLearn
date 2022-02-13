def merge(result, arr):
    
    (m,n) = (len(result), len(arr))
    (res, i, j, k) = ([], 0, 0, 0)
    
    while k<m+n:
        
        if m==i:
            res.extend(arr[j:])
            break
            
        elif n==j:
            res.extend(result[i:])
            break
            
        elif result[i] < arr[j]:
            res.append(result[i])
            i,k = i+1, k+1
            
        else:
            res.append(arr[j])
            j,k = j+1, k+1
            
    return res

def mergeKLists(L):
    result = []
    size = len(L)
    while(size!=0):
        result = merge(result, L[size-1])
        size-=1
        
    return result
    
k = int(input())
LL=[]
for i in range(k):
    subL = [int(item) for item in input().split(" ")]
    LL.append(subL)
print(*mergeKLists(LL))