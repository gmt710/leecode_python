class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        List_matrix = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    List_matrix.append([i,j])
                    
        for i,j in List_matrix:
            matrix[i] = [0]*len(matrix[i])
            for k in range(len(matrix)):
                matrix[k][j] = 0

        
