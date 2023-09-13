class Solution {
public:
    int solve(vector<int> &cost,int n,vector<int> &dp){
        if(n==0||n==1){
            return cost[n];
        }
        else if(dp[n]!=-1){
            return dp[n];
        }
        else{
            dp[n] = cost[n]+min(solve(cost,n-1,dp),solve(cost,n-2,dp));
            return dp[n];
        }

    }

    int minCostClimbingStairs(vector<int>& cost) {
        int i,n = cost.size();
        vector<int> dp(n+1,-1);
        int ans = min(solve(cost,n-1,dp),solve(cost,n-2,dp));
        return ans;


    // int minCostClimbingStairs(vector<int>& cost) {
    //     int i,n = cost.size();
    //     // int dp[n] = {0};
    //     vector<int> dp(n,0);
    //     dp[0] = cost[0];
    //     if (n>1){
    //         dp[1] = cost[1];
    //     } 
            
    //     for(i=2;i<n;i++){
    //         dp[i] =  cost[i]+min(dp[i-1],dp[i-2]);
    //         }
    //     return min(dp[n-1],dp[n-2]);
    // }

    }
};


