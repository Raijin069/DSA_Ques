class custom_sort(str):
    def __lt__(x: str, y: str):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 0:
            return ""
        if n == 1:
            return str(nums[0])

        nums = [str(num) for num in nums]
        nums.sort(key=custom_sort)
        ans = ''.join(nums)
        return "0" if ans[0] == "0" else ans