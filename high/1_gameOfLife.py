class Solution(object):
    
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        def Life(board_org,board, m, n):
            # up:上边界;
            # down:下边界
            # left:左边界
            # right:右边界
            if len(board_org) == 1:
                up = 0
                down = 0
            else:
                if m == 0:
                    up = 0
                    down = m+1
                elif m == (len(board_org)-1):
                    up = m-1
                    down = m
                else:
                    up = m-1
                    down = m+1
            if len(board_org[0]) == 1:
                left = 0
                right = 0
            else:
                if n == 0:
                    left = 0
                    right = n+1
                elif n == (len(board_org[0])-1):
                    left = n-1
                    right = n
                else:
                    left = n-1
                    right = n+1
            a = []
            # from collections import Counter
            for i in range(up,down+1):
                for j in range(left,right+1):
                    print(i,j)
                    if i == m and j ==n:
                        continue
                    a.append(board_org[i][j])
            count = a.count(1)
            if board_org[m][n] == 1:
                if count < 2 or count > 3:
                    board[m][n] = 0
            else:
                if count == 3:
                    board[m][n] = 1
             
        # 细胞的出生和死亡是同时发生的，说明出生与死亡状态由下一个状态由当前状态决定
        board_org = [[board[k][t] for t in range(len(board[0]))] for k in range(len(board))]
        for m in range(len(board)):
            for n in range(len(board[0])):
                Life(board_org,board,m,n)
                
                    
