class Solution(object):
    def findIsland(self, grid, i ,j, m, n):
        if grid[i][j] == '1':
            grid[i][j] = '0'
            if i-1 >= 0:
                self.findIsland(grid, i-1, j, m, n)
            if i+1 < m:
                self.findIsland(grid, i+1, j, m, n)
            if j-1 >= 0:
                self.findIsland(grid, i, j-1, m, n)
            if j+1 < n:
                self.findIsland(grid, i, j+1, m, n) 
        return
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 深度优先思想。遍历矩阵的每个元素，
        # 如果为1则计数加一，同时把自己和周围的元素都置0。
        if len(grid) == 0 or not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                # List[List[str]] 应该是字符型
                if grid[i][j] == '1':
                    count += 1
                    self.findIsland(grid, i, j, m, n)               
        return count
