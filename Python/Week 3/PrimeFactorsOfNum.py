num = int(input())

"""if(num==2):
    print('2')"""
if(num==1):
    print('1')

for i in range(2,num+1):
    flag = True
    if(num%i==0):
        for j in range(2,i):
            if(i%j == 0):
                flag=False
                break
        if(flag==True):
            print(i)

