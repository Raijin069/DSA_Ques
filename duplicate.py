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
    
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        str1 = strs[0]
        str2 = strs[-1]
        index = 0
        while(index<len(str1)):
            if (str1[index]==str2[index]):
                index+=1
            else:
                break

        if index==0:
            return ""
        return str1[0:index]               



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

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1]*n
        product_before_current = 1
        product_after_current = 1

        for i in range(n):
            res[i]=product_before_current
            product_before_current*=nums[i]

        
        for i in range(n-1,-1,-1):
            res[i]*=product_after_current
            product_after_current*=nums[i]

        return res     
        
        
        # n=len(nums)
        # left_pr=[1]*n
        # right_pr=[1]*n
        # product_array = []
        # for i in range(1,n):
        #     left_pr[i] = left_pr[i-1]*nums[i-1]
        #     right_pr[i] = nums[::-1][i-1]*right_pr[i-1]
        #     print("left =",left_pr[i],"right=",right_pr[i]," nums",nums[i-1])
        # for i in range(n):
        #     product_array.append(left_pr[i]*right_pr[::-1][i])  
        # return product_array   
         

        
            






                   
        
        
        
           
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

# S = "aabaa"

# print(result.removeConsecutiveCharacter(S))

# strs = ["dog","racecar","car"]
# print(result.longestCommonPrefix(strs))

nums=[1,2,3,4]
print(result.productExceptSelf(nums))