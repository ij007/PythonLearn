def is_perfect(company):
    
    candidate = list(company.values())
    flag = 0
    for i in range(len(candidate)):
        if candidate[i] in candidate[i+1:] :
            return False
    return True
print(is_perfect(eval(input().strip())))