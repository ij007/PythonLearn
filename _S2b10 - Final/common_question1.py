weight = input().split(',')
weight = list(map(int, weight))

max_weight = max(weight)
weight.remove(max_weight)
weight_sum = sum(weight)

count = 1

while( len(weight)!=0 ):
    
    if(len(weight) == 0):
        print(count)
        break
        
    if(sum(weight)<max_weight):
        print(count)
        break
    
    else:
        rem_max = max(weight)
        max_weight+=rem_max
        weight.remove(rem_max)
        count+=1
        
if(len(weight) == 0):
        print(count)