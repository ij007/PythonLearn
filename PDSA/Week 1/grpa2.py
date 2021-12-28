def find_prime(num):
    l = [2]
    i=3

    while(i<num):
        flag = True
        
        for j in range(2,i):
            if(i%j == 0):
                flag = False
                
        if flag == True:
            l.append(i)
        
        i+=1
    return l
        
def Goldbach(n):
    
    l = find_prime(n)
    ans = []
    for head in range(len(l)):
        for tail in range(head,len(l)):
            if (l[head]+l[tail] == n):
                ans.append((l[head], l[tail]))
    return ans  
n=int(input())
print(sorted(Goldbach(n)))