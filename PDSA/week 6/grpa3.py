def mh(a,k):
    l=2*k+1
    r=2*k+2
    mini=k
    if l<len(a) and a[l]>a[k]:
        mini=l
    if r<len(a) and a[r]>a[mini]:
        mini=r
    if mini!=k:
        a[k],a[mini]=a[mini],a[k]
        mh(a,mini)
        
def min_max(arr):
    x=int((len(arr)//2)-1)
    for i in range(x,-1,-1):
        mh(arr,i)