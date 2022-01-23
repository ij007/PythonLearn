class Queue():
    def __init__(self):
        self.queue = []
        
    def addq(self, data):
        self.queue.append(data)
        
    def delq(self):
        v = None
        if(not self.isempty()):
            v = self.queue[0]
            self.queue = self.queue[1:]
            
        return v
        
    def isempty(self):
        
        return(self.queue==[])
        
    def __str__(self):
        
        print(str(self.queue))
        
def bfsList(alist, start):
    
    q = Queue()
    
    visited = {}
    
    for i in alist.keys():
        visited[i] = False
    
    visited[start] = True
    q.addq(start)
    
    while(not q.isempty()):
        j = q.delq()
        for i in alist[j]:
            if(not visited[i]):
                visited[i] = True
                q.addq(i)
    
    return visited
def findComponents_undirectedGraph(vertices, edges):

    alist = {}
    for i in vertices:
        alist[i] = []
        
    for i,j in edges:
        
        alist[i].append(j)
        alist[j].append(i)
     
    comp = {}
    
    for i in vertices:
        comp[i] = -1
        
    (compid,seen) = (0,0)
    
    while(seen < len(vertices)):
        start = min([i for i in alist.keys() if comp[i] == -1])
        
        visited = bfsList(alist, start)
        
        for i in visited.keys():
            if(visited[i]):
                comp[i] = compid
                seen+=1
        
        compid+=1
        
    return (max(comp.values())+1)