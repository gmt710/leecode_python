class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        """
        1.如果起始跳一阶的话，剩余的n-1阶就有 f(n-1) 种跳法；
        2.如果起始跳二阶的话，剩余的n-2阶就有 f(n-2) 种跳法；
        所以f(n) = f(n-1) + f(n-2)，实际结果即为斐波纳契数。
        即前(n-2)与前(n-1)阶方法之和
        """
        if n == 0: return 1
        if n == 1: return 1
        
        tmpList = [1, 1]
        for i in range(0, n-1):
            x = tmpList[-1] + tmpList[-2]
            tmpList.append(x)
        return tmpList[-1]
    

        
