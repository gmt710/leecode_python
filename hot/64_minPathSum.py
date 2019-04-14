class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r = len(grid) # 行数
        c = len(grid[0]) # 列数
        dp = [[0]*c for _ in range(r)] # 初始化全0矩阵
        dp[0] = [sum(grid[0][:i+1]) for i in range(c)] # 计算出第0行
        temp = list(zip(*grid))[0] # 矩阵的转置，取出第0行
        
        for i in range(r):
            dp[i][0] = sum(temp[:i+1])
        for i in range(1, r):
            for j in range(1, c):
                 dp[i][j] = min(dp[i-1][j], dp[i][j-1])+grid[i][j] # 自下而上的递推赋值
        
        return dp[r-1][c-1]

       
