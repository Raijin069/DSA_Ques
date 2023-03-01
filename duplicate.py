class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        ans = [-1,-1]
        size = len(A)
        count = {i:0 for i in range(1,size+1)}
        # print(count)
        for i in range(size):
            count[A[i]] +=1 
        # print(count)
        for key,value in count.items():
            if value==2:
                ans[0] = key
                continue
            if value==0:
                ans[1] = key
        return ans      

    def containsDuplicate(self, nums: list[int]) -> bool: 
        size = len(nums)
        count = {i:0 for i in range(1,size+1)}
        # print(count)
        for i in range(size):
            count[nums[i]] +=1 
        # print(count)
        for key,value in count.items():
            if value>1:
                return True     
        return False       

    def maxSubArray(self, nums: list[int]) -> int: 
        maxsum = nums[0]
        currsum = 0
        for i in range(len(nums)):
            currsum = max(nums[i],currsum+nums[i])
            maxsum = max(maxsum,currsum)
        return maxsum

    def isPalindrome(self, s: str) -> bool:
        ans = ""
        for i in s:
            if i.isalnum():
                ans+=i
        # print(s)
        s=ans.lower()
        # print(s)
        if s == s[::-1]:
            return True 
        return False   

    def isAnagram(self, s: str, t: str) -> bool:
        # if set(s) == set(t):
        #     return True
        # return False
        
        count_s = {i:0 for i in s}
        count_t = {i:0 for i in t} 
        
        for i in s:
            count_s[i] +=1 
        for i in t:
            count_t[i] +=1
        if count_t == count_s:
            return True
        return False 


    def print_duplicate(self, s: str):
        count_s= {i:0 for i in s}

        for i in s:
            count_s[i] +=1

        for key, value in count_s.items():
            if value>1:
                print(key)
    
    def removeConsecutiveCharacter(self, S):
        ans=""
        ans+=S[0]
        for i in range(1,len(S)):
            if S[i-1]!=S[i]:
                ans+=S[i]
        return ans

    def isValid(self, s: str) -> bool:
        # while '()' in s or '[]'in s or '{}' in s:
        #     s = s.replace('()', '')
        #     s = s.replace('{}', '')
        #     s = s.replace('[]', '')
        # if len(s)==0:
        #     return True
        # return False
        stack = []
        bracket_pair = {"(":")","{":"}","[":"]"} 
        for bracket in s:
            if bracket in bracket_pair:
                stack.append(bracket) 
            elif len(stack)==0 or bracket!=bracket_pair[stack.pop()]:
                return False

        return(len(stack) == 0)        


                   
        
        
        
           
result = Solution()
# A = (3 ,1 ,2 ,5 ,3)
# nums = [1,2,3,5,4]
# s = "A man, a plan, a canal: Panama"
# print(result.repeatedNumber(A))    
# print(result.containsDuplicate(nums)) 
# nums =  [5,4,-1,7,8]      
# print(result.maxSubArray(nums)) 
# print(result.isPalindrome(s))
# s = "anagram"
# t = "nagaram"
# s = "rat"
# t = "car"
# s = "AseemSreeraj"
# print(result.isAnagram(s,t))
# print(result.print_duplicate(s.lower()))]

S = "aabaa"
print(result.removeConsecutiveCharacter(S))


