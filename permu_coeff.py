def p(n,k):
    ans = 1 
    for i in range(n,n-k,-1):
        ans*=i
    print(ans)