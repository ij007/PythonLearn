#GRPA 3

class TimeConverter :
    
    def __init__(self,seconds):
        
        self.seconds = seconds
        
    def Second_to_Minutes(self):
        
        minutes = self.seconds//60
        seconds = self.seconds%60
        
        return f"{minutes} min {seconds} sec"
        
    def Second_to_Hours(self):
        
        hours = self.seconds//3600
        minutes = (self.seconds%3600)//60
        seconds = self.seconds%60
        
        return f"{hours} hr {minutes} min {seconds} sec"
        
    def Second_to_Days(self):
        
        days = (self.seconds//86400)
        hours = (self.seconds%86400)//3600
        minutes = (self.seconds%3600)//60
        seconds = self.seconds%60
        
        return f"{days} days {hours} hr {minutes} min {seconds} sec"
    
sec = int(input())
a = TimeConverter(sec)
print(a.Second_to_Minutes())
print(a.Second_to_Hours())
print(a.Second_to_Days())