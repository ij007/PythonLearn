def isBlock(l) :

    length1 = abs(l[1][0] - l[0][0])
    length2 = abs(l[3][0] - l[2][0])

    height2 = abs(l[3][1] - l[2][1])
    height1 = abs(l[1][1] - l[0][1])

    if(length1==length2 and height2==height1):
        return True

    else:
        return False


print(isBlock([(0, 0), (1, 0), (1, 1), (0, 1)]))
