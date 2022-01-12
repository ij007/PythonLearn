def EvaluateExpression(string):
    l = string.split(' ')
    ans = []
    for i in l:
        try:
            ans.append(int(i))
        except:
            b=(ans.pop())
            a=(ans.pop())
            if(i == '*'):
                ans.append((a*b))
            elif(i == '**'):
                ans.append((a**b))
            elif(i == '-'):
                ans.append((a-b))
            elif(i == '/'):
                ans.append((a/b))
            elif(i == '+'):
                ans.append((a+b))
    return ans[0]
print(float(EvaluateExpression(input())))