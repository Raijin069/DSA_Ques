def knapsnap(N,W,wt,val):
    def solve(n,cap):
        if n==0 or cap == 0:
            return 0
        else:
            curr_wt = wt[n-1]
            curr_val = val[n-1]
            if curr_wt <= cap:
                c1 = curr_val + solve(n-1,cap-curr_wt)
                c2 = solve(n-1,cap)
                return max(c1,c2)
            else:
                return solve(n-1,cap)
    return solve(N,W)

def knapsnap_dp(N,W,wt,val):
    dp = {}
    def solve(n,cap):
        if n==0 or cap == 0:
            return 0
        elif (n,cap) in dp:
            return dp[(n,cap)]    
        else:
            curr_wt = wt[n-1]
            curr_val = val[n-1]
            if curr_wt <= cap:
                c1 = curr_val + solve(n-1,cap-curr_wt)
                c2 = solve(n-1,cap)
                c =  max(c1,c2)

            else:
                c = solve(n-1,cap)
            dp[(n,cap)] = c
            return c     
    return solve(N,W)                    

