side1 = int(input())
side2 = int(input())
side3 = int(input())


if ((side1**2) == (side2**2) + (side3**2)) or ((side2**2) == (side1**2) + (side3**2)) or ((side3**2) == (side2**2) + (side1**2)):
    print('YES')
    
else:
    print('NO')