def min_cost(wl, source, destination):
    (rt, visited, distance) = ({}, {}, {})
        
    for i in wl.keys():
        visited[i] = False
        distance[i] = 1000000
        rt[i] = []
            
    distance[source] = 0
    rt[source] = [source]
        
    for i in wl.keys():
        mindist = min([distance[vertice] for vertice in wl.keys() if not visited[vertice]])
        
        vertexL = [i for i in wl.keys() if not visited[i] and distance[i] == mindist]
        
        if vertexL == []: break
    
        nextV = min(vertexL)
        visited[nextV] = True
        
        for childV, dist in wl[nextV]:
            if distance[childV] > dist+distance[nextV]:
                distance[childV] = dist+distance[nextV]
                rt[childV] = rt[nextV] + [childV]
        
    #print(rt[destination])        
    return distance[destination],rt[destination]
def min_cost_walk(wl, s, d, v):
    d1, p1 = min_cost(wl, s, v)
    d2, p2 = min_cost(wl, v, d)
    
    return (d1+d2,p1[0:len(p1)-1]+p2)
size = int(input())
edges = eval(input())
S= int(input())
D=int(input())
V=int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
print(min_cost_walk(WL,S, D, V))