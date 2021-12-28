def consolidate(student):
    
    console={}
    
    for index in student:
        for subject in index:
            if subject not in console:
                console[subject] = 1
            else:
                console[subject]+=1
                
    return console
    
def popular(console):
    
    maxnum=0
    popsubj = ''
    
    for keys,items in console.items():
        
        if items>maxnum:
            maxnum = items
            popsubj = keys
            
    return popsubj