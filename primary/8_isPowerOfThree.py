class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 对n取以3为底的对数k， 若3**k == n, 则该数为3的幂次方
        if n > 0:
            if 3**round(math.log(n,3)) == n:
                return True
            else:
                return False
        else:
            return False
        
            
            
        
