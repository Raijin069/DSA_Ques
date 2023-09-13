class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        n1 = len(matrix[0])
        f_c = False
        
        for i in range(n):
            if target<=matrix[i][-1]:
                f_c = True
                break

        if f_c:
            low = 0
            high = n1 - 1
        
            while low <= high:
        
                mid = (high + low) // 2
     
                if matrix[i][mid] < target:
                    low = mid + 1

                elif matrix[i][mid] > target:
                    high = mid - 1

                else:
                    return True
        
            return False
        return False