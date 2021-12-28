#GRPA 2

import math

class Point :
    
    def __init__(self,x = 0,y = 0):
        
        self.x = x
        self.y = y
        
    def move(self, dx, dy):
        
        self.x = self.x + dx
        self.y = self.y + dy
        
    def value(self):
        
        return (self.x,self.y)
    
    def duplicate(self):
        
        return Point()
        
class Line() :
    
    def __init__(self, startPoint, endPoint):
        
        self.startPoint = startPoint
        self.endPoint = endPoint
        
    def length(self) :
        x = self.startPoint.value()
        y = self.endPoint.value()
        
        xlen = (x[0]-y[0])**2
        ylen = (x[1]-y[1])**2
        
        lengt = math.sqrt(xlen+ylen)
        return lengt
        
    def slope(self):
        
        x = self.startPoint.value()
        y = self.endPoint.value()
        
        xlen = (x[0]-y[0])
        ylen = (x[1]-y[1])
        
        if(xlen==0):
            return math.inf
        
        slp = ylen/xlen
        
        return slp
        

pt1 = Point()
pt2 = pt1.duplicate()

inp1 = input().strip().split(',')
inp2 = input().strip().split(',')

pt1.move(int(inp1[0]),int(inp1[1]))
pt2.move(int(inp2[0]),int(inp2[1]))

print(f'Point 1: {pt1.value()}')
print(f'Point 2: {pt2.value()}')

l1 = Line(pt1, pt2)
print(f'Line length: {l1.length():.2f}')
print(f'Line slope: {l1.slope():.2f}')