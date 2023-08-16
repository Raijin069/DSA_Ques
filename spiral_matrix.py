res = [0 for i in range(100)]

class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        top, bottom, left, right = 0, len(matrix), 0, len(matrix[0])
        c = 0

        while left<right and top<bottom:
            for i in range(left,right):
                res[c] = matrix[top][i]
                c+=1
            top+=1

            for i in range(top,bottom):
                res[c] = matrix[i][right-1]
                c+=1
            right-=1

            if not (left<right and top<bottom):
                break 
            
            for i in range(right-1,left-1,-1):
                res[c] = matrix[bottom-1][i]
                c+=1
            bottom-=1

            for i in range(bottom-1,top-1,-1):
                res[c] = matrix[i][left]
                c+=1
            left+=1

        
        return res[:c]