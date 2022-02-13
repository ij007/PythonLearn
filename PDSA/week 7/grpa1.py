def minbin(num,init):
  import math
  mini = math.inf
  min_bin = 0
  for key in init:
    if (num + init[key]) < mini:
      min_bin = key
      mini = (num + init[key])
  return min_bin

def minimizeLateness(n,jobs):
  newj = []
  for (h,u,v) in jobs:
    newj.append((v,u,h))
  newj.sort()

  init = {}
  for i in range(n):
    init[i] = 0
  bins  = [[] for x in range(n)]

  for job in newj:
    min_bin = minbin(job[1], init)
    bins[min_bin].append(job[2])
    init[min_bin] = init[min_bin] + job[1]
  return bins