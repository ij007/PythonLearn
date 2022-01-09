def mergeInPlace(A,B):
    m,n = len(A),len(B)
    j = 0
    for i in range(m):
        for j in range(n):
            if(A[i]>B[j]):
                A.swap(i,B,j)
    for i in range(n):
        for j in range(i+1,n):
            if(B[i]>B[j]):
                B.swap(i,B,j)