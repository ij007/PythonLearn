def merge(D1, D2, priority):
    
    for keys in D1:
        
        if keys in D2 :
            
            if( priority == 'first' ):
                
                D2[keys] = D1[keys]
                
            else:
                
                D1[keys] = D2[keys] 
                
        else :
            
            D2[keys] = D1[keys]
            
    return D2
            
