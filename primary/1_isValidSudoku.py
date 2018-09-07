class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        block_3 = [[] for i in range(9)]
        col = [[] for i in range(9)]
        row = [[] for i in range(9)]
        
        for row_i, row_j in enumerate(board):
            for col_i, num in enumerate(row_j):
                if num != '.':
                    k = (row_i//3)*3 + (col_i//3)
                    if num in block_3[k]+col[col_i]+row[row_i]:
                        return False
                    block_3[k].append(num)
                    col[col_i].append(num)
                    row[row_i].append(num)
        return True
    
                    
