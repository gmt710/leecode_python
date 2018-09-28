class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        res = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                # 此处的可能性等于左侧与上侧可能性之和
                res[i][j] = res[i-1][j] + res[i][j-1]
        return res[-1][-1]
        
