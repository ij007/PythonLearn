s = str(input())
l2=[]
while(s!=""):
    l=[] 
    for item in s.split(' '):
        l.append((item))
    l2.append(l)
    s= str(input())
l4=[]
for x in range(len(l2[0])):
    l3=[]
    for y in range(len(l2)):
        l3.append(l2[y][x])
    l4.append(l3)    
l4.reverse()
for x1 in range(len(l4)):
    for y1 in range(len(l4[0])):
        if (y1 == (len(l4[0])-1)):
            print(l4[x1][y1])
        else:
            print(l4[x1][y1],end=' ')