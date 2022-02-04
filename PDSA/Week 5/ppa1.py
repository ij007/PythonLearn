import sys
class XYZ_Courier():
    
    def __init__(self,wl):
        self.wl = wl
        
    def cost(self, source, destination):
        
        (visited, distance) = ({}, {})
        
        for vertices in self.wl.keys():
            
            visited[vertices] = False
            distance[vertices] = 10000000000
            
        distance[source] = 0
        
        for vertices in self.wl.keys():
            
            #getting minimum distance
            nextd = min([distance[v] for v in self.wl.keys() if not visited[v]])
            
            #choosing vertex for minimum distance
            nextvL = [v for v in self.wl.keys() if not visited[v] and distance[v] == nextd]
            
            
            if nextvL == []: break
        
            nextV = min(nextvL)
            visited[nextV] = True
        
            for childV, dist in self.wl[nextV]:
                if not visited[childV]:
                    distance[childV] = min(distance[childV], distance[nextV]+dist)
                    
                    
        return distance[destination]*5

    def route(self, source, destination):
        
        (rt, visited, distance) = ({}, {}, {})
        
        for i in self.wl.keys():
            visited[i] = False
            distance[i] = 1000000
            rt[i] = []
            
        distance[source] = 0
        rt[source] = [source]
        
        for i in self.wl.keys():
            mindist = min([distance[vertice] for vertice in self.wl.keys() if not visited[vertice]])
            
            vertexL = [i for i in self.wl.keys() if not visited[i] and distance[i] == mindist]
            
            if vertexL == []: break
        
            nextV = min(vertexL)
            visited[nextV] = True
            
            for childV, dist in self.wl[nextV]:
                if distance[childV] > dist+distance[nextV]:
                    distance[childV] = dist+distance[nextV]
                    rt[childV] = rt[nextV] + [childV]
                    
        return rt[destination]
size = int(input())
edges = eval(input())
s=int(input())
d=int(input())
WL = {}
for i in range(size):
    WL[i] = []
for ed in edges: #for create list for undirected graph
    WL[ed[0]].append((ed[1],ed[2]))
    WL[ed[1]].append((ed[0],ed[2]))
C = XYZ_Courier(WL)
print(C.cost(s,d))
print(C.route(s,d))