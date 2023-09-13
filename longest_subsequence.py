class Solution:
    def longestSubsequence(self, N, a):
        l = [1 for _ in range(N)]
        for i in range(1,N):
            for j in range(i):
                if abs(a[i]-a[j])==1:
                    l[i] = max(l[i],l[j]+1)
        ans = 0
        return max(ans,max(l))