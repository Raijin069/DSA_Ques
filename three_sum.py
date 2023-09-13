class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        if n<3:
            return []
        target = 0
        nums.sort()
        s = set()
        output = []
        for i in range(n):
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        output = list(s)
        return output