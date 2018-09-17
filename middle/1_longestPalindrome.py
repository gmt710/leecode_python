class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_s = s[:]
        if str_s[::-1] == s:
            return s
        
        for i in range(1,len(s)):
            j = 0
            while j <= i:
                str_s = s[j:len(s)-i+j]
                if  str_s[::-1] == str_s:
                    return str_s
                j += 1
        
