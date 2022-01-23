ans = []
class Stack():
    
    def __init__(self):
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        v = None
        if not self.isempty():
            v = self.stack[-1]
            self.stack = self.stack[:-1]
        return v
    
    def top(self):
        v = None
        if not self.isempty():
            v = self.stack[-1]
        return v
    
    def isempty(self):
        return (self.stack == [])
        
    def pstack(self):
        return str(self.stack)
    
def findpath(alist, source, dest, visited, path):
    
    visited[source] = True
    path.append(source)
    
    if source == dest:
        ans.append(''.join(path))
        
    else:
        
        for i in alist[source]:
            if visited[i] == False:
                findpath(alist, i, dest, visited, path)
                
    path.pop()
    visited[source] = False
    
    
def findAllPaths(v, alist, source, dest):
    
    
    visited = {}
    for i in v:
        visited[i] = False
    
    path = []
    findpath(alist, source, dest, visited, path)
            
    return ans
    
#Vertices are expected to be labelled as single letter or single digit 

#Sort and arrange the result for uniformity
def ArrangeResult(result):
  res = []
  for item in result:
    s = ""
    for i in item:
      s += str(i)    
    res.append(s)
  res.sort() 
  return res

v = [item for item in input().split(" ")]
Alist = {}
for i in v:
  Alist[i] = [item for item in input().split(" ") if item != '']
source = input()
dest = input()
print(ArrangeResult(findAllPaths(v, Alist, source, dest)))