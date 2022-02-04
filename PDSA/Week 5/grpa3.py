def IsNegativeWeightCyclePresent(wl):
    distance = {}
    s = min(list(wl.keys()))
    for u in wl.keys():
        distance[u] = 9999999
      
    distance[s] = 0
    r = len(list(wl.keys()))
    for i in range (r-1):
        for u in wl.keys():
            for v,d in wl[u]:
                distance[v] = min(distance[u]+d, distance[v])
                
    
    for u in wl.keys():
        for v,d in wl[u]:
            if(distance[u]+d < distance[v]):
                return True
    return False
size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    
print(IsNegativeWeightCyclePresent(WL))