n= int(input())

matrix = []

for rows in range(n):
    
    elems = (input()).strip().split(',')
    row = []
    
    for columns in range(n):
        
        row.append(int(elems[columns]))
        
    matrix.append(row)
    
operation = str(input())

if(operation == 'row'):
    for row in range(-1, -n-1,-1):
        for i in range(n-1):
            print(matrix[row][i],end=',')
        print(matrix[row][-1])
        
else:
    for row in range(n):
        for i in range(-1,-n,-1):
            print(matrix[row][i],end=',')
        print(matrix[row][0])