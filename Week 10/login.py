# GRPA 4

class UserLoginInfo:
    
    def __init__(self,userName,password):
        
        self.userName = userName
        self.password = [password]
        
    def ChangePassword(self,newpassword):
        
        if(newpassword not in self.password):
            
            if(newpassword[0].isupper() and newpassword[0].isalpha() and len(newpassword)>7 and newpassword[1:].isalnum()):
                
                self.password.insert(0,newpassword)
                return 'Password updated successfully'
                
            else:
                return 'Invalid password'
                
        else:
            
            return 'Password already used'
            
    def Login(this, username , password):
        
        if(this.userName == username and this.password[0] == password ):
            
            return f'Welcome {this.userName}'
            
        else:
            
            return 'Username or Password incorrect'
            
    def RetrievePassword(this):
        
        return this.password[0]
        
u1 = UserLoginInfo(input(),input())
a = u1.ChangePassword(input())
b = u1.ChangePassword(input())
c = u1.ChangePassword(input())
d = u1.Login(input(),input())
e = u1.Login(input(),input())
f = u1.RetrievePassword()
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)