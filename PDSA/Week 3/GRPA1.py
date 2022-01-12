def DishPrepareOrder(ord_list):
    d = {}
    for i in ord_list:
        try:
            d[i]+=1
        except KeyError:
            d[i]=1
    ans = []
    d_invert = {} 
    for key, value in d.items():
        try:
            d_invert[value].append(key)
        except KeyError:
            d_invert[value] = [key]
            
    while(d_invert!={}):
        ans.extend(sorted(d_invert[max(d_invert)]))
        d_invert.pop(max(d_invert))
    
    return ans
nums = eval(input())
print(DishPrepareOrder(nums))