def highest_grossing(yearFrom, yearUpto, genre):
    
    file = open('IMDB_reviews.csv','r')
    dataset = file.readlines();
    
    highestGross = 0
    name=''

    for records in dataset[1:]:
        
        records = records.split(',')
        #print(records)
        
        #print(records[-1].strip())
        glist = records[4].split(' ')
        
        if (genre in records[4].split(' ')) :

            
            if yearFrom <= int(records[2].strip()) :
                
                if (int(records[2].strip()) <= yearUpto):
        
                    if records[9].strip()!='' and highestGross < int(records[9].strip()):
                        highestGross = int(records[9].strip())
                        name = records[1]
                
    file.close()
            
    return name