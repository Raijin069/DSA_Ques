class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        x,low,high = -1,0,n-1
        
        while low <= high:

            mid = low + (high - low)//2

            if nums[mid] == target:
                x = mid
                break

            elif nums[mid] < target:
                low = mid + 1

            else:
                high = mid - 1
        
        if x==-1:
            return [-1,-1]

        start,end = x,x
        
        while end<n-1:
            if nums[end+1]==target:
                end+=1
            else:
                break
        
        while start>0:
            if nums[start-1]==target:
                start-=1
            else:
                break

        return [start,end]   