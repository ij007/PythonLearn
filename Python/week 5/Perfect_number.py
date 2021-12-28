def perfect_number(num):
    ans=0
    for i in range(1,num):
        if(num%i==0):
            ans+=i
    if(ans==num):
        return True
    else:
        return False

