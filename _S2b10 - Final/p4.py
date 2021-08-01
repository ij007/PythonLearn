words = eval(input())
freq = {}

for word in words:
    
    if word.lower() not in freq:
        freq[word.lower()] = 1
    else:
        freq[word.lower()]+=1
for i in sorted(freq):
    print(f'{i}:{freq[i]}')