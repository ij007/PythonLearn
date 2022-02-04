def min_cost(wl, source, destination):
    
    (rt, distance) = ({}, {})
    
    for i in wl.keys():
        rt[i] = []
        distance[i] = 10000000000000
        
    
    distance[source] = 0
    rt[source] = [source]
    
    for u in wl.keys():
        for v in wl.keys():
            for childV, cost in wl[v]:
                if(distance[childV] > cost+distance[v]):
                    rt[childV] = rt[v]+[childV]
                    distance[childV] = cost+distance[v]
                    
    return (distance[destination], rt[destination])
    
size = int(input())
edges = eval(input())
s = int(input())
d = int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for directed graph
    WL[ed[0]].append((ed[1],ed[2]))
print(min_cost(WL,s,d))