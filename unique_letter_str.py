class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        l = [[-1] for _ in range(26)]

        for i in range(n):
            l[ord(s[i])-65].append(i)

        for i in range(26):
            l[i].append(n)

        count = 0

        for i in range(26):
            for j in range(1,len(l[i])-1):
                count += (l[i][j] - l[i][j-1])*(l[i][j+1] - l[i][j])
        return count