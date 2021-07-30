def process_line(i):
    
    sumelement=0
    product=1
    with open('numbers.txt','r') as file:
        lines = file.readlines()
        
        if(len(lines) <i):
            return tuple([-1,-1,-1])
            
        element = lines[i].strip().split(',')
        
        for i in range(len(element)):
            sumelement+=int(element[i])
            product*=int(element[i])
        
        
        return tuple([len(element),sumelement, product])