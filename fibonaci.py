def fib(n:int,dp:dict)->int:
    if n == 0 or n == 1:
        return n
    elif dp[n]!=-1:
        return dp[n]
    else:
        dp[n] = fib(n-1,dp) + fib(n-2,dp)
        return dp[n]        

n=950
dp = [-1]*(n+1)
print(fib(n,dp))    