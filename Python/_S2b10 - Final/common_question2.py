def isPrime(num):
    
    for i in range(2,num//2+1,1):
        if num%i == 0:
            return False
            
    return True

n = int(input())

for i in range(2,n,1):
    
    if (i+2) <= n :
        if isPrime(i) and isPrime(i+2):
            
            print(f'{i},{i+2}')