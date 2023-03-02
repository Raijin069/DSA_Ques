def print_duplicate(s:str):
    count = {i:0 for i in s}
    ans={}
    for i in s:
        count[i]+=1
    # print(count)
    for key,value in count.items():
        if value>1:
            ans[key] = value  
    print(ans)
    
s="geeksforgeeks"
print_duplicate(s)            
    