def preprocessing(maze):
  m, n = len(maze), len(maze[0])
  S, E, K = None, None, None
  AList = {}
  for i in range(m):
    for j in range(n):
      AList[(i,j)] = []
      allowedTiles = [' ', '*']
      if maze[i][j] in allowedTiles:
        if i+1 < m and maze[i+1][j] in allowedTiles: 
          AList[(i,j)].append((i+1, j))
        if 0 <= i-1 and maze[i-1][j] in allowedTiles: 
          AList[(i,j)].append((i-1, j))
        if j+1 < n and maze[i][j+1] in allowedTiles:
          AList[(i,j)].append((i, j+1))
        if 0 <= j-1 and maze[i][j-1] in allowedTiles:
          AList[(i,j)].append((i, j-1))
        if j == 0: S = (i,j)
        if j == n-1: E = (i,j)
        if maze[i][j] == '*': K = (i,j)
  return AList, S, E, K

# Do a BFS maintaining level information to get the number of steps required.
def BFS(AList, x):
  visited = {k:False for k in AList.keys()}
  level = {k:None for k in AList.keys()}
  q = []

  visited[x] = True
  level[x] = 0
  q.append(x)
  while len(q) > 0:
    v = q.pop(0)
    visited[v] = True
    for i in AList[v]:
      if not visited[i]:
        q.append(i)
        if level[i] == None:
          level[i] = level[v] + 1
  from pprint import pprint
  return level

maze = []
line = input()
while line:
  maze.append(line)
  line = input()

AList, S, E, K = preprocessing(maze)
level = BFS(AList, S)
if level[K] == None:
  print(-1)
else:
  level2 = BFS(AList, K)
  if level2[E] == None:
    print(-2)
  else:
    print(level[K] + level2[E])