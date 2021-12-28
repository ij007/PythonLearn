import math
class Triangle:
    def __init__(self,p=0,q=0,r=0):
        
        l = sorted([p,q,r])
        self.a = l[0]
        self.b = l[1]
        self.c = l[2]
            
    
    def is_valid(self):
        if(self.a + self.b > self.c and self.a + self.c > self.b and self.c + self.b > self.a):
            return 'Valid'
        else:
            return 'Invalid'
    
    def Side_Classification(self):
        
        if(self.is_valid()=='Valid'):
            
            if(self.a == self.b == self.c):
                return 'Equilateral'
            elif(self.a == self.b or self.b == self.c or self.c == self.a):
                return 'Isosceles'
            else:
                return 'Scalene'
            
        else:
            return self.is_valid()
            
    def Angle_Classification(self):
        
        if(self.is_valid() == 'Valid'):
            if(self.a**2 + self.b**2 > self.c**2):
                return 'Acute'
            elif(self.a**2 + self.b**2 == self.c**2):
                return 'Right'
            elif(self.a**2 + self.b**2 < self.c**2):
                return 'Obtuse'
        else:
            return self.is_valid()
            
    def Area(self):
        if(self.is_valid()=='Valid'):
            s = (self.a+self.b+self.c)/2
            return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        else:
            return self.is_valid()
a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())