def collatz_repeat(n):
    
    count = 0
    
    while(n!=1):
    
        if( n%2 == 0 ):
            
            n = n/2
            count+=1
            
        else:
            
            n = 3*n + 1
            count+=1
    
    return count 