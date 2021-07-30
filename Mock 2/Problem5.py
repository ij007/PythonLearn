class Book():
    def __init__(self, name, author, pages, genre):
        
        self.name = name
        self.author = author
        self.pages = pages
        self.genre = genre
        
    def is_fiction(self):
        return True if self.genre=='Fiction' else False
        
    def is_nonFiction(self):
        return True if self.genre=='Nonfiction' else False
        
    def same_author(self, book):
        
        return True if self.author == book.author else False
        
    def time_to_read(self):
        
        if self.pages<100:
            return '5 days'
            
        if 100<=self.pages<=500:
            return '20 days'
            
        if self.pages>500:
            return 'infinite'

# Please enter your answer above this code
inp1 = input().strip().split(',')
inp1[2] = int(inp1[2])
inp2 = input().strip().split(',')
inp2[2] = int(inp2[2])

book1 = Book(*inp1)
book2 = Book(*inp2)
                        
print(book1.is_fiction(), book1.is_nonFiction(), book1.time_to_read())
print(book2.is_fiction(), book2.is_nonFiction(), book2.time_to_read())
print(book1.same_author(book2))