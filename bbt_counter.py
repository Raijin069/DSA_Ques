class Solution:
    def countBT(self, h):
        if h == 1 or h==0:
            return 1
        if h==2:
            return 3
        mod = 1000000007
        dp = [0 for i in range(h+1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 3
        for i in range(3,h+1):
            i_1 = dp[i-1]%mod 
            dp[i] = ((i_1)*((2*dp[i-2]%mod) + i_1))%mod
        return dp[h]