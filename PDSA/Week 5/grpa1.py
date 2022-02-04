def FiberLink(wl):
    (edges, component) = ([], {})
    
    for u in wl.keys():
        component[u] = u
        edges.extend([(d,u,v) for v, d in wl[u]])
        
    edges.sort()
    cost = 0
    for d,u,v in edges:
        if component[u] != component[v]:
            cost+=d
            c = component[u]
            for i in wl.keys():
                if component[i] == c:
                    component[i] = component[v]
                    
    return cost
size = int(input())
edges = eval(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges:
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(FiberLink(WL))