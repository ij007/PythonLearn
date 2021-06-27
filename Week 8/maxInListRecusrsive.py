def max_element(input_list) :
    
    if(len(input_list)==1):
        return input_list[0]
        
    maxNum = max_element(input_list[1:])
    
    if(maxNum < input_list[0]):
        maxNum = input_list[0]
    
    return maxNum