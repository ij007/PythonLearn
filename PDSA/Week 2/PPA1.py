count=0
def binarySearchIndexAndComparisons(L,k):
    global count
    if(L == []):
        return (False,count)
    if (len(L)==0 and k!=L[0]):
        count += 1
        return ((False,count))
    
    mid = (len(L)-1)//2
    
    if(L[mid] == k):
        count+=1
        return (True,count)
    elif(L[mid] < k):
        count+=1
        return binarySearchIndexAndComparisons(L[mid+1:],k)
    else:
        count+=1
        return binarySearchIndexAndComparisons(L[:mid],k)
