class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        # if k>len(nums) divide by k and get remainder
        k = k % len(nums)
    
        # Reverse the entire array
        nums=nums[::-1]
    
        # Reverse the first k elements
        nums[:k] = nums[:k][::-1]
    
        # Reverse the remaining elements
        nums[k:] = nums[k:][::-1]
        
        return nums


nums = [1,2,3,4,5,6,7]
k = 3        
s1=Solution()
print(s1.rotate(nums,k))
