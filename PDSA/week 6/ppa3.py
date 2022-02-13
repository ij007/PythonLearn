from collections import deque
# Helper function
class myStack:
  def __init__(self):
    self.Q = deque()
  
  def pop(self):
    return self.Q.pop()

  def push(self, x):
    return self.Q.append(x)

  def isempty(self):
    return False if self.Q else True

# Checks using BFS if the graph is connected excluding the node exCamp
def isConnectedExcluding(Alist, exCamp):
  vertices = [v for v in Alist.keys() if v!=exCamp]
  visited ={k:False for k in vertices}
  st = myStack()
  st.push(vertices[0])

  while not st.isempty():
    curr = st.pop()
    visited[curr] = True
    for (v, d) in Alist[curr]:
      if (v != exCamp and not visited[v]):
        st.push(v)

  # Check if all are visited
  return all(value == True for value in visited.values())

# Do not remove the site from graph, rather exclude it from each comparision and calculation.
def connectCamps(Alist, exCamp):
  # Check if the graph is connected
  if not isConnectedExcluding(Alist, exCamp):
    return -1
  
  edges, te = [], []
  components, members, size = {}, {}, {}
  minCost = 0
  
  # Create edge list and union find data structure excluding exCamp connected edges
  for u in Alist.keys():
    if (u != exCamp):
      edges.extend([(d,u,v) for (v,d) in Alist[u] if v!=exCamp])
      components[u], members[u], size[u] = u, [u], 1
  
  edges.sort()

  # For undirected graph remove duplicate edges
  distinctEdges = [edges[0]]
  for i in range(len(edges)-1):
    if not ((edges[i][0] == edges[i+1][0]) 
         and edges[i][1]==edges[i+1][2] and edges[i][2]==edges[i+1][1]):
      distinctEdges.append(edges[i+1])
  edges=distinctEdges

  # Calculate MST and minimum cost
  for (d,u,v) in edges:
    if (components[u] != components[v]):
      te.append((u,v))
      minCost += d
      c_old = components[u]
      c_new = components[v]
      for k in members[c_old]:
        components[k] = c_new
        members[c_new].append(k)
        size[c_new] += 1

  return minCost