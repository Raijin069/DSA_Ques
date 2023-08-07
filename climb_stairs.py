class Solution:
    def climbStairs(self, n: int) -> int:
        if(n<4):
            return n

        a = 3
        b = 2
        for i in range(n-3):
            a+=b
            b=a-b 
        return a

        # arr = [0 for i in range(n+1)]
        # arr[1] = 1
        # arr[2] = 2
        # for i in range(3,n+1):
        #     arr[i] = arr[i-1]+arr[i-2]
        # return arr[n]