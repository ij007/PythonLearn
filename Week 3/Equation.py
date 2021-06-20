#x^4+y^3==z^2

n = int(input())
for i in range(1, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if i**4 + j**3 == k**2:
                print(i, j, k)