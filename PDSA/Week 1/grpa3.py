def odd_one(L):
    
    d={}
    for i in L:
        try:
            if(type(i) == str):
                d['str']+=1
            if(type(i) == bool):
                d['bool']+=1
            if(type(i) == int):
                d['int']+=1
            if(type(i) == float):
                d['float']+=1
                
        except KeyError:
            if(type(i) == str):
                d['str']=1
            if(type(i) == bool):
                d['bool']=1
            if(type(i) == int):
                d['int']=1
            if(type(i) == float):
                d['float']=1
    
    key = list(d.keys())
    val = list(d.values())
    if val[0]>val[1]:
        return key[1]
    else:
        return key[0]
    
    
print(odd_one(eval(input().strip())))