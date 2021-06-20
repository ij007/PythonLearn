num = int(input())
mystr = ''
count=0
num = list(str(num))

for i in num :
    
    if(i=='1'):
        print('one')
        if(count>0):
            mystr+='One'
        else:
            mystr+='one'
        count+=1
        
    elif(i=='2'):
        print('two')
        if(count>0):
            mystr+='Two'
        else:
            mystr+='two'
        count+=1
        
    elif(i=='3'):
        print('three')
        if(count>0):
            mystr+='Three'
        else:
            mystr+='three'
        count+=1
        
    elif(i=='4'):
        print('four')
        if(count>0):
            mystr+='Four'
        else:
            mystr+='four'
        count+=1
        
    elif(i=='5'):
        print('five')
        if(count>0):
            mystr+='Five'
        else:
            mystr+='five'
        count+=1
        
    elif(i=='6'):
        print('six')
        if(count>0):
            mystr+='Six'
        else:
            mystr+='six'
        count+=1
        
    elif(i=='7'):
        print('seven')
        if(count>0):
            mystr+='Seven'
        else:
            mystr+='seven'
        count+=1
        
    elif(i=='8'):
        print('eight')
        if(count>0):
            mystr+='Eight'
        else:
            mystr+='eight'
        count+=1
        
    elif(i=='9'):
        print('nine')
        if(count>0):
            mystr+='Nine'
        else:
            mystr+='nine'
        count+=1
        
    elif(i=='0'):
        print('zero')
        if(count>0):
            mystr+='Zero'
        else:
            mystr+='zero'
        count+=1

print(mystr)