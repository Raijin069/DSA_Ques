class Solution:
	def maxSubstring(self, S):
	    arr = [1 if i == "0" else -1 for i in S]
	    max_sum = arr[0]
	    curr_sum = 0
	    n = len(S)
	    for i in range(n):
	        curr_sum = max(arr[i],curr_sum+arr[i])
	        max_sum = max(max_sum,curr_sum)
	    if max_sum<0:     
	        max_sum = -1
	    return max_sum 