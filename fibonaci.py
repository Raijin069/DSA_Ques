def fib_dp(n:int,dp:list)->int:
    if n == 0 or n == 1:
        return n
    elif dp[n]!=-1:
        return dp[n]
    else:
        dp[n] = fib_dp(n-1,dp) + fib_dp(n-2,dp)
        return dp[n]        

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)    


n=50
dp = [-1]*(n+1)
# for i in range(n+1):
#     print(i , " = ",fib_dp(i,dp))  
print(fib_dp(n, dp))      
# print(fib(n))      