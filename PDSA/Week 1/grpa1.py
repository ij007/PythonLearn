def find_Min_Difference(L,P):
    l = sorted(L)
    mind = 10000
    head,tail=(0,P-1)
    while(tail<len(l)):
        if(l[tail]-l[head] < mind):
            mind = l[tail]-l[head]
        tail+=1
        head+=1
    return mind
L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))