bracecount = 0 
depth = 0 
inp = input() 
 
for ch in inp: 
    if ch == '(': 
        bracecount+=1 
        depth = bracecount if depth < bracecount  else depth 
    elif ch == ')': 
        bracecount-=1 
     
    if bracecount < 0: 
        break; 
 
if bracecount == 0: 
  print(depth) 
else: 
    print('Not matched')