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
        return(self.queue == [])
        
    def __str__(self):
        return(str(self.queue))

def findConnectionLevel(vertices, amat, x, y):
    
    (visited, parent) = ({}, {})
    
    q = Queue()
    
    (row, col) = (vertices, vertices)
    
    for i in range(row):
        visited[i] = -1
        parent[i] = -1
        
    visited[x] = 0
    q.addq(x)
    
    while(not q.isempty()):
        j = q.delq()
        for i in range(len(amat[j])):
            if(amat[j][i] == 1 and visited[i] == -1):
                visited[i] = visited[j]+1
                parent[i] = j
                q.addq(i)
    
    if(visited[x] == -1 or visited[y] == -1):
        return 0
        
    else:
        return(visited[y])
    
vertices = int(input())
Amat = []
for i in range(vertices):
  row = [int(item) for item in input().split(" ")]
  Amat.append(row)
personX = int(input())
personY = int(input())
print(findConnectionLevel(vertices, Amat, personX, personY))