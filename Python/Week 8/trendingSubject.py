def trending(subject_topics):
    
    common_topics_list =[]
    
    for x in range(len(subject_topics)):
        
        for y in range(len(subject_topics[x])):
            
            if(subject_topics[x][y]) not in common_topics_list:
                
                common_topics_list.append(subject_topics[x][y])
                
    d1={}
    
    
    for x1 in range(len(common_topics_list)):
        d1[common_topics_list[x1]]=0
        
    for x in range(len(subject_topics)):
        
        k1 = list(set(subject_topics[x]))
        
        for y in range(len(k1)):
            
            #print(k1[y])
            d1[k1[y]]+=1
            
    max1 =0
    
    max2=''
    
    
    min1=10000
    min2=''
    
    for x2 in d1:
        
        if(d1[x2]> max1):
            
            max1 = d1[x2]
            max2 = x2
            
        if(d1[x2]<min1):
            
            min1 = d1[x2]
            min2=x2
            
    max3 = sum(value == max1 for value in d1.values())
    min3 = sum(value == min1 for value in d1.values())
    
    return(max3,min3)