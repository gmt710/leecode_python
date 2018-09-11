class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'}': '{', ']': '[', ')': '('}
        # 为了占位置
        stack = [0]
        for i in s:
            if i in d and d[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
            
        if len(stack) == 1:
            return True
        else:
            return False
