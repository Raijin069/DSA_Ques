class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n,cnt = len(nums),1
        if n==1:
            return nums[0]
        nums.sort()
        for i in range(1,n):
            if(nums[i]==nums[i-1]):
                cnt+=1
            else:
                if cnt>n/2:
                    return nums[i-1]
                cnt = 1
        if cnt>n/2:
            return nums[i-1]
        return -1