def no_overlap(L):
    L.sort(key = lambda x:x[2])
    res = []
    current = L[0]
    res.append(L[0])
    for i in L[1:]:
        if i[1] > current[2]:
            current = i
            res.append(i[0])
            
    return res