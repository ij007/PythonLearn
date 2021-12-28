class Triangle :
    
    def __init__(self, a, b, c):
        
        self.a = a
        self.b = b
        self.c = c
        
        self.valid = ''
        if self.a + self.b + self.c == 180 :
            self.valid = True
        else: 
            self.valid = False
        
    def is_right(self):
        
        if self.a == 90 or self.b == 90 or self.c == 90 :
            return True 
        else: 
            return False
        
    def is_obtuse(self):
        
        if self.a > 90 or self.b > 90 or self.c > 90:
            return True 
        else: 
            return False
        
    def is_acute(self):
        
        if self.a < 90 and self.b < 90 and self.c < 90:
            return True 
        else: 
            return False