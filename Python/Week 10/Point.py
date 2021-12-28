#GRPA 1

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
            
        
        
pt1 = Point()
pt2 = pt1.duplicate()

inp1 = input().strip().split(',')
inp2 = input().strip().split(',')

pt1.move(int(inp1[0]),int(inp1[1]))
pt2.move(int(inp2[0]),int(inp2[1]))

print(f'Point 1: {pt1.value()}')
print(f'Point 2: {pt2.value()}')