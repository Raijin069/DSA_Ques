# class Solution {
# public:
#     int maxProfit(vector<int>& prices) {
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        profit,max_profit = 0,0
        mini = prices[0]
        if n==0:
            return 0
        for i in range(0,n):
            current = prices[i]
            if(mini>current):
                mini = current
            profit = current-mini
            if(max_profit<profit):
                max_profit = profit
        
        return max_profit
