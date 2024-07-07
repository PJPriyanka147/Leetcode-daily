class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m , n = len(matrix), len(matrix[0])
        zero_positions = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_positions.append((i, j))

        for i, j in zero_positions:
            for col in range(n):
                matrix[i][col] = 0
            for row in range(m):
                matrix[row][j] = 0
        
        
