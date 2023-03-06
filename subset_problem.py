def subset_sum(arr,N,sum):
    def solve(n,cap):
        if cap==0:
            return 1
        elif n==0:
            return 0
        else:
            curr_num = arr[n-1]
            if curr_num <= cap:
                c1 = solve(n-1,cap-curr_num)
                c2 = solve(n-1,cap)
                return c1 or c2
            else:
                return solve(n-1,cap)
    return solve(N,sum)                 

def subset_sum_dp(arr,N,sum):
    dp = {}
    arr.sort(reverse = True)
    def solve(n,cap):

        if cap==0:
            return 1
        elif n==0:
            return 0
        elif (n,cap) in dp:
            return dp[(n,cap)]     
        else:
            curr_num = arr[n-1]
            if curr_num <= cap:
                c1 = solve(n-1,cap-curr_num)
                c2 = solve(n-1,cap)
                c = c1 or c2
            else:
                c =  0 
            dp[(n,cap)] = c
            return c 
    return solve(N,sum)                              


            
    
