class Solution:
    def maximum69Number (self, num: int) -> int:
        s = [i for i in str(num)]
        n = len(s)
        for i in range(n):
            if s[i] == "6":
                s[i] = "9"
                break
        ans = 0
        for i in range(n):
            ans=int(s[i])+10*ans
        return ans
        