class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        c = set(s)
        count_s = collections.Counter(s)
        count_t = collections.Counter(t)
        for i in c:
            if count_s[i] != count_t[i]:
                return False
        return True
            
