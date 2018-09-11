class Solution(object):
#     def romanmean(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if s == 'M':
#             count = 1000
#         if s == 'D':
#             count = 500
#         if s == 'C':
#             count = 100
#         if s == 'L':
#             count = 50
#         if s == 'X':
#             count = 10
#         if s == 'V':
#             count = 5
#         if s == 'I':
#             count = 1
        
#         return count
            
    
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         count = 0
#         print(len(s))
#         for i in range(len(s)-1):
#             if self.romanmean(s[i]) < self.romanmean(s[i+1]):
#                 count -=self.romanmean(s[i])
#             else:
#                 print(i)
#                 count += self.romanmean(s[i])
#         return count + self.romanmean(s[-1])
    
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        convert = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1} 
        print(len(s))
        for i in range(len(s)-1):
            if convert[s[i]] < convert[s[i+1]]:
                count -=convert[s[i]]
            else:
                print(i)
                count += convert[s[i]]
        return count + convert[s[-1]]
                
                    
