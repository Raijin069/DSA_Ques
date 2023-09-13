class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        prime=[0 for _ in range(n)]
        count = 0
        for i in range(2,n):
            if prime[i]==0:
                for j in range(i*i,n,i):
                    prime[j]=1

        
        for i in range(2,n):
            if prime[i]==0:
                count+=1
        return count