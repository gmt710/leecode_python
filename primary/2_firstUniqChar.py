class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        count = collections.Counter(s)
        print(count)
        for i in range(len_s):
            if count[s[i]] == 1:
                return i
        return -1
