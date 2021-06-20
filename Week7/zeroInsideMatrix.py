rows = int(input())
cols = int(input())


arr=[]

for i in range(rows):
    
    row  = input().split(' ')
    
    arr.append([])
    
    for j in range(cols):
        
        arr[i].append(int(row[j]))
    
for i in range(1,rows-1):
    
    for j in range(1,cols-1):
        
        arr[i][j] = 0
        
for i in range(rows):
    
    for j in range(cols):
        
        if( j == cols-1 ):
            print(arr[i][j])
        else:
            print(arr[i][j], end=' ')
        
   
