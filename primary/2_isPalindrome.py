class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
#         set_strnum = ['a','b','c','d','e','f','g','h','i','j',
#                       'k','l','m','n','o','p','q','r','s','t',
#                       'u','v','w','x','y','z',
#                       '0','1','2','3','4','5','6','7','8','9']
#         t = s.lower()
#         for i in range(len(s)):
#             if s[i] not in set_strnum:
#                 t = t.replace(s[i],'') 
#         lens = len(t)
#         if lens <= 1:
#             return True
#         l = 0
#         r = lens - 1

#         while l<=r:
#             if t[l] != t[r]:
#                 return False
#             l += 1
#             r -= 1
#         return True

        # def f(i):
        #     q = i.isalpha()
        #     if 48<=ord(i)<=57:
        #         p = 1
        #     else:
        #         p = 0
        #     return q or p
        # l = list(filter(f, s))
        # s = ''.join(l)
        # s = s.upper()
        # return s[::] == s[::-1]
        # l = list(filter(str.isalnum,s.lower()))
        # if l[::] == l[::-1]:
        #     return True
        # else:
        #     return False
        
        s = list(filter(str.isalnum, str(s.lower())))
        if s == s[::-1]:
            return True  
        else:
            return False
        
        
