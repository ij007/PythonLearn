def is_magic(mat):
    res = 0
    row_sum=0
    col_sum=0
    diag_sum=0
    length = len(mat[0])
    
    for i in range(length):
        res+=mat[0][i]
    
    for row_count in range(1,length):
        row_sum=0
        for col_count in range(length):
            row_sum+=mat[row_count][col_count]
        if(res!=row_sum):
            return 'NO'
            
    for col_count in range(length):
        col_sum=0
        for row_count in range(length):
            col_sum+=mat[row_count][col_count]
        if(res!=col_sum):
            return 'NO'
    
    for diag_count in range(length):
        diag_sum+=mat[diag_count][diag_count]
    
    if(diag_sum!=res):
        return 'NO'
    diag_sum=0     
    for i,j in zip(range(length),range(length-1,-1,-1)):
        diag_sum+=mat[i][j]
        
 
    if(diag_sum!=res):
        return 'NO'
    
    return 'YES'
        