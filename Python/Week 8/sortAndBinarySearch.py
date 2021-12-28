def simple_sort(item_list) :
    
    n = len(item_list)

    for i in range(n):
        
        already_sorted = True
        
        for j in range(n - i - 1):
            
            if item_list[j] > item_list[j + 1]:
                
                item_list[j], item_list[j + 1] = item_list[j + 1], item_list[j]
                
                already_sorted = False

        if already_sorted:
            
            break
        
    return item_list;
    
def simple_search(item_list,item):
    
    
    start = 0
    end = len(item_list)
    mid = (start+(end-start))//2
    
    if (len(item_list)<2 and item_list[0]!= item ):
        
        return False
    
    if (len(item_list)<2 and item_list[0] == item):
            
            return True
   
    if(item == item_list[mid]):
        
        return True 
            
    elif(item > item_list[mid]):
            
        return simple_search(item_list[mid:],item)
            
    elif(item_list[mid] > item):
            
        return simple_search(item_list[:mid],item)
