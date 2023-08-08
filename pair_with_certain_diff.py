class Solution:
    def maxSumPairWithDifferenceLessThanK(self, arr,n, k): 
        arr.sort()
        i,sum=n-1,0
        while i>0:
            if arr[i]-arr[i-1]<k:
               sum+=arr[i]+arr[i-1]
               i-=2
            else:
                i-=1
        return sum