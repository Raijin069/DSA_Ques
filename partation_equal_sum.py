def equal_partation(arr:list,n):
    sol1 = "no"
    sol2 = "yes"
    dp = {}
    sm = sum(arr)
    if sm&1==1:
        return sol1
    sum_cal = sm//2
    def solve(n,cap):
        if n==0:
            return sol1
        elif cap==0:
            return sol2
        elif (n,cap) in dp:
            return dp[(n,cap)]    
        else:
            curr_num = arr[n-1]
            if curr_num <= cap:
                c1 = solve(n-1,cap-curr_num)
                c2 = solve(n-1,cap)
                c = c1 or c2
            else:
                c = 0        
            dp[(n,cap)] = c
            return c