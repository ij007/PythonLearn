words = eval(input())

eng_dict = {}
for word in words:
    if word[0].lower() not in eng_dict:
        eng_dict[word[0].lower()] = [word.lower()]
    else:
        if(word.lower() not in eng_dict[word[0].lower()]):
            eng_dict[word[0].lower()].append(word.lower())
for i in sorted(eng_dict.keys()):
    print(f'{i}: ', end='')
    print(*sorted(eng_dict[i]))