import string

label = str(input())

words = list(label)

alphabets = {}
alphabet_string = string.ascii_uppercase
count=1

for c in alphabet_string :
    alphabets[c]=count
    count+=1

n = len(words)-1
outputNum = 0

for word in words:
    outputNum+=(26**n)*alphabets[word]
    n-=1
    
print(outputNum)