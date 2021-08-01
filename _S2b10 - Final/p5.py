import string

num = ['0','1','2','3','4','5','6','7','8','9']
numlen = len(num)-1

small_alpha = list(string.ascii_lowercase)
small_alpha_len = len(small_alpha)-1

big_alpha = list(string.ascii_uppercase)
big_alpha_len = len(big_alpha)-1

word = str(input())
code = ''

for letter in word:
    
    if letter in num:
        code += str(num[numlen - num.index(letter)])
    
    elif letter in small_alpha:
        code+= str( small_alpha[small_alpha_len - small_alpha.index(letter)])
        
    elif letter in big_alpha:
        code+= str( big_alpha[big_alpha_len - big_alpha.index(letter)])
    
    elif letter == ' ':
        code+='_'
    
    else:
        code+=letter
        
print(code)