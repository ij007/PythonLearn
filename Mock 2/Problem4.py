f = open('file.txt', 'w')
while True:
    line = input()
    if line == '':
        break
    f.write(line+'\n')
f.close()
sentence_count = 0
word_count = 0
max_sentence = ''
max_count=0
word_freq = {}


with open('file.txt','r') as file:
    lines = file.readlines()
    
    sentence_count = len(lines)
    
    for line in lines:
        words = line.strip().split(' ')
        
        word_count+= len(words)
        
        if len(words)>max_count:
            max_count = len(words)
            max_sentence = ' '.join(words)
        
        for word in words:
            
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word]+=1

unique = list(word_freq.keys())
print(eval(input().strip()))