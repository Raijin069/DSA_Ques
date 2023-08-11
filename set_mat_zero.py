class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        r = set()
        c = set()
        n = len(matrix)
        n1 = len(matrix[0])
        for row in range(n):
            for col in range(n1):
                if matrix[row][col] == 0:
                    r.add(row)
                    c.add(col)

        for i in r:
            matrix[i] = [0 for _ in range(n1)]
        
        for j in c:
            for i in range(n):
                matrix[i][j] = 0