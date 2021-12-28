import math
mylist =[]
while True:
  n = input()
  if n != "END":
    mylist.append(float(n))
  else:
    break

mean = sum(mylist)/(len(mylist))

dev = 0
for i in mylist:
    dev += (i-mean)**2

stddev = math.sqrt(dev/(len(mylist)-1))
print("{0:.02f}".format(stddev))