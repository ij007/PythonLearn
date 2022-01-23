class Queue:
  def __init__(self):
    self.queue = []
  def addq(self,v):
    self.queue.append(v)
  def delq(self):
    v = None
    if not self.isempty():
      v = self.queue[0]
      self.queue = self.queue[1:]
    return(v)
  def isempty(self):
    return(self.queue == [])
  def __str__(self):
    return(str(self.queue))

def BFS(graph, v):
  visited = {}
  for node in graph:
    visited[node] = False
  q = Queue()
  visited[v] = True
  q.addq(v)
  
  while not(q.isempty()):
    to_explore = q.delq()
    for neighbour in graph[to_explore]:
      if not(visited[neighbour]):
        visited[neighbour] = True
        q.addq(neighbour)
  return visited

def findMasterTank(vertices, edges):
  graph = {}
  for vertex in vertices:
    graph[vertex] = []
  for edge in edges:
    graph[edge[0]] = graph[edge[0]] + [edge[1]]
  
  indegree = {}
  for node in graph:
    indegree[node] = 0
  for node in graph:
    for neigh in graph[node]:
      indegree[neigh] = indegree[neigh] + 1
  
  vlist = list(indegree.values())
  zeros = [(str(vlist.index(x)+1)) for x in vlist if x == 0]

  for zn in zeros:
    visited = BFS(graph,zn)
    if vertices == [node for node in visited if visited[node] == True]:
      return zn
  return 0
v = [item for item in input().split(" ")]
#Tanks(vertices) numbered from 1 to n in string format.
numberOfEdges = int(input())
e = []
for i in range(numberOfEdges):
  s = input().split(" ")
  e.append((s[0], s[1]))
print(findMasterTank(v, e))