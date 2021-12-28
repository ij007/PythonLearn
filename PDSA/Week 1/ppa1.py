def isPrime(n):
    import math
    if(n==1 or n==4 or n==2):
        return False
    for i in range(3,n):
        if(n%i) == 0:
            return False
    return True
    
def Twin_Primes(n,m):
    primes=[]
    while(n<m):
        if(isPrime(n) and isPrime(n+2)):
            primes.append(tuple([n,n+2]))
            n+=2
        else:
            n+=1
    return primes
    
n=int(input())
m=int(input())
print(sorted(Twin_Primes(n, m)))