def solution():
    '''
    1. Process version_1.txt and version_2.txt
    2. Print the number lines in version_2.txt that are not in version_1.txt
    '''
    
    file2 = open('version_2.txt', 'r')
    
    count = 0 
    flag=0
    
    line2 = file2.readline()
    
    while(line2 != ''):
        
        if(line2 != '') :
            
            file1 = open('version_1.txt','r')
            flag = 0
            line1 = file1.readline()
            
            while(line1 != '') :
                
                if line1 == line2 :
                    
                    flag = 1
                    break
                
                line1 = file1.readline()
        
            
            if(flag == 0):
               # print(line2)
                count+=1
                
            file1.close()
            line2 = file2.readline()
                
    file2.close()
    print(count)