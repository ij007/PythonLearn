def c(o):
    v = int(o[1:])
    return v
def combinationSort(l):
    d={}
    l1 = []
    l2 = []
    for i in range(len(l)):
        m = list(l[i])
        if m[0] not in d:
            d[m[0]] = [l[i]]
        else:
            d[m[0]] += [l[i]]
    while d!={}:
        a = min(d)
        k = list(d[a])
        j = sorted(k,reverse = True, key = c)
        l1 += k
        l2 += j
        d.pop(a)
    return(l1,l2)