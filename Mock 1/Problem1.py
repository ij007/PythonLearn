def printSeq(sl, n, flist):
    if n==0:
        print(flist)
        return
        
    for i in range(len(sl)):
        newlist=flist+sl[i]
        printSeq(sl, n-1, newlist)

iword = str(input())

wordlist = list(iword)
sortedlist = []

for i in range(3):
    
    sortedlist.append(min(wordlist))
    wordlist.remove(min(wordlist))
    
printSeq(sortedlist,3,'')