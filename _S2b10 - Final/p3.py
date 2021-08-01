TEST_CASE = (input())
n = int(input())
head = input().split(',')
students = {}

for index in range(n):
    
    details = input().split(',')
    
    students[int(details[0])] = {}
    
    for insidehead in range(1,len(head),1):
        
        students[int(details[0])][head[insidehead]] = int(details[insidehead])
        

    