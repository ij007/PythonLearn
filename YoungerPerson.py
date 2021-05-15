name1 = str(input())
dob1 = str(input())
name2 = str(input())
dob2 = str(input())

if (int(dob1[6:10]) == int(dob2[6:10])):
    if(name1<name2):
        print(name1)
    else:
        print(name2)
elif (int(dob1[6:10]) > int(dob2[6:10])):
    print(name1)
else:
    print(name2)