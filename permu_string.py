class Solution:
    def check_permu(self, d1: dict, s2: str):
        d2 = {}
        for i in s2:
            if i not in d2:
                d2[i]=0
            d2[i]+=1
        return d1==d2

    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1,l2 = len(s1),len(s2)
        if l1>l2:
            return False
        d1 = {}
        for i in s1:
            if i not in d1:
                d1[i]=0
            d1[i]+=1
        s1_set = d1.keys()
        for i in range(l1,l2+1):
            n=i-l1
            if s2[n] in s1_set:
                if self.check_permu(d1,s2[n:i]):
                    return True
        return False
