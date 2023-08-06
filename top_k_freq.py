class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d1 = {}
        for i in nums:
            if i not in d1:
                d1[i]=0
            d1[i]+=1
            
        ans = [0 for _ in range(k)]
        
        d1 = [[key,value] for key,value in d1.items()]
        d1.sort(key = lambda x:x[1],reverse=True)
        for i in range(k):
            ans[i] = d1[i][0]
        return ans