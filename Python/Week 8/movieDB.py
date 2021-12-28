def add_movie_to_boxoffice(movies_db, new_movie):
    
    movies_db[new_movie[0]] = [new_movie[1],new_movie[2]]
    return movies_db

def highest_grossing_movie_year(movies_db):
    
    year=''
    highest = 0
    
    for keys in movies_db:
        
        if(movies_db[keys][0]>highest):
            
            highest = movies_db[keys][0]
            
            year = movies_db[keys][1]
        
    return year
    
def total_collection(movies_db):
    
    total = 0
    
    for keys in movies_db:
        
        total+=movies_db[keys][0]
        
    return total
    
def average_collection(movies_db):
    
    count = len(movies_db)
    
    total = total_collection(movies_db)
    
    average = round((total/count),2)
    
    return average
    
def num_of_movies_above_average_movies(movies_db):
    
    
    count=0
    average = average_collection(movies_db)
    
    for keys in movies_db:
        
        if(movies_db[keys][0] > average):
            
            count+=1
            
    return count





# Suffix Code Block - start
def suffix_block():
    global movies_db
    movies_db = add_movie_to_boxoffice(movies_db, new_movie)
    print(total_collection(movies_db))
    print(average_collection(movies_db))
    print(num_of_movies_above_average_movies(movies_db))
    print(highest_grossing_movie_year(movies_db))
# Suffix Code Block - end