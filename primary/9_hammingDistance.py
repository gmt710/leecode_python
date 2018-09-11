class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        import collections
        str_xy = str(bin(x ^ y))
        n_count = collections.Counter(str_xy)
        return n_count['1']
