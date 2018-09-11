class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        import collections
        str_n = str(bin(n))
        n_count = collections.Counter(str_n)
        return n_count['1']
        
        
