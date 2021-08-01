def placement(p,q):
    if p==q:
        return 'on'
    if p>q:
        return 'below'
    if p<q:
        return 'above'
print(placement(*eval(input().strip())))