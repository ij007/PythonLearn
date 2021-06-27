def reverse(input_list) :

    if (len(input_list))==1 :
        ans=input_list
        return ans

    ans=[]
    ans = reverse(input_list[1:]) + input_list[:1]
    return ans
    
