s,ans = "my name is aseem gupta"," "
s=s.split(" ")[::-1]
for i in s:
    ans+=i[::-1]+" "
print(ans)