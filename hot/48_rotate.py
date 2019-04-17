class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        if len(matrix) == 0 or len(matrix[0]) == 0: return []
        r = len(matrix)
        c = len(matrix[0])
        for i in range(r):
            for j in range(i+1,c):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
        
        for i in range(r):
            matrix[i] = matrix[i][::-1]
            
