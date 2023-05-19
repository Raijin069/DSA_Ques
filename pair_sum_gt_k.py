def isPossible(a,b,n,k):
    a.sort()
    b.sort(reverse=True)
    flag=0
    for i in range(n):
        if a[i]+b[i]<k:
            flag=1
            break
    if flag==1:
        return "hell no"
    return "oh yes"

a = [1, 2, 2, 1 ]
b = [3, 3, 3, 4 ]
k = 5
n =len(a)
print(isPossible(a,b,n,k))    

