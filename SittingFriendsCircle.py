emp1=int(input())
emp2=int(input())
emp3=int(input())
emp4=int(input())
emp5=int(input())

if((emp1+emp2)%2==0 and (emp3+emp2)%2==0 and (emp3+emp4)%2==0 and (emp4+emp5)%2==0 and (emp5+emp1)%2==0):
    print("YES")
else:
    print("NO")