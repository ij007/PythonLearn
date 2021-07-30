start = int(input())
end = int(input())

byThree = []
byFive = []

for num in range(start,end+1,1):
    
    if num%3 == 0:
        byThree.append(num)
        
    if num%5 == 0:
        byFive.append(num)
        
    
o1 = set(byThree).union(set(byFive))
o2 = set(byThree).intersection(set(byFive))
o3 = set(byThree).difference(set(byFive))
o4 = set(byFive).difference(set(byThree))
print(sorted(o1))
print(sorted(o2))
print(sorted(o3))
print(sorted(o4))