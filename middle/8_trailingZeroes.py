class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 求0也就是求其中2*5的个数，也就是5的个数，
        # 因为每一个偶数都含2，只要有5肯定有2。
        r = 0
        while n >= 5:
            n = n // 5
            r+=n
        return r
    
