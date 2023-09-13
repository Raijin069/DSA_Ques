class Solution:

    def nextPermutation(self, nums: list[int]) -> None:
 
        idx,n = -1,len(nums)
        for i in range(n-1,0,-1):
            if(nums[i]>nums[i-1]):
                idx=i
                break
        print(idx)
        if(idx==-1):
            nums = nums[::-1]
        else:
            prev = idx
            for i in range(idx+1,n):
                if(nums[i]>nums[idx-1] and nums[i] <= nums[prev]):
                    prev=i
            nums[prev],nums[idx-1]=nums[idx-1],nums[prev]
            i,j=idx,n-1
            while i < j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        print(nums)
  
sol1 = Solution()
sol1.nextPermutation([3,2,1])