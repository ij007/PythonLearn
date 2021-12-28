sum=0
num = int(input())
flag = False

if(num>2):
    sum+=2
    for i in range(2,num):
        for j in range(2,i):
            if(i%j==0):
                flag = False
                break
            else:
                flag = True
            
        if(flag == True):
            sum+=i
elif(num==2):
    sum+=2

            
print(sum)