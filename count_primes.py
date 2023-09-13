class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        prime=[False for _ in range(n)]
        count = 0
        for i in range(2,n):
            if prime[i]==False:
                for j in range(i*i,n,i):
                    prime[j]=True

        
        for i in range(2,n):
            if prime[i]==False:
                count+=1
        return count