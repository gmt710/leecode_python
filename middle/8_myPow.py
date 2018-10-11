class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x > 100.0 or x < -100.0:
            return None
        
        res = x**n
        if res < -2**31 or res > 2**31-1:
            return None
        else:
            return res
        
