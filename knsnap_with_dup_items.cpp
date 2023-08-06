class Solution{
public:
    int dp[1001][1001];
    int solve(int i,int j,int val[],int wt[]){
        if(i<=-1){
            return 0;
        }
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        if(wt[i]>j){
            return dp[i][j] = solve(i-1,j,val,wt);
        }
        
        int op1 = val[i]+solve(i,j-wt[i],val,wt);
        int op2 = solve(i-1,j,val,wt);
        
        return dp[i][j] = max(op1,op2);
    }
    
    int knapSack(int N, int W, int val[], int wt[])
    {
        memset(dp,-1,sizeof(dp));
        return solve(N-1,W,val,wt);
    }
};

