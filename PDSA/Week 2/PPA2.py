def sortInRange(L,r):
    d = {}
    for i in L:
        try:
            d[i]+=1
        except KeyError:
            d[i]=1
    
    L.clear()
    for i in range(r):
        L.extend([i]*d[i])
        
    return L