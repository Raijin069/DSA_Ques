class Solution: 

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = {}
        if not cost:
            return 0
        n = len(cost)
        dp = [0 for _ in range(n)]
        dp[0] = cost[0]
        if n>1: 
            dp[1] = cost[1]
        for i in range(2,n):
            dp[i] =  cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[-1],dp[-2])

        
        # def solve(cost,n):
        #     if n==0 or n==1:
        #         return cost[n]
        #     elif n in dp:
        #         return dp[n]
        #     else:
        #         c = cost[n] + min(solve(cost,n-1),solve(cost,n-2))
        #     dp[n] = c
        #     return c
        # return min(solve(cost,n-1),solve(cost,n-2))