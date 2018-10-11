class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for word in s:
            print(word)
            res = res*26 + ord(word)-ord('A')+1
        return res
    
