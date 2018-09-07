class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        now = '1'        
        for i in range(1,n):
            count = 1
            str_n = ''
            for j in range(len(now)):
                if (j+1) < len(now) and now[j] == now[j+1]:
                    count += 1
                else:
                    str_n += str(count)+ now[j]
                    count = 1
            now = str_n
        return now
        
#         now = '1'
#         for k in range(1, n):
#             out = ''
#             i = 0
#             while i < len(now):
#                say = now[i]
#                count = 1
#                while i < len(now) -1 and now[i] == now[i+1]:
#                   count += 1
#                   i += 1
#                out += str(count)+say
#                i += 1
#             now = out

#         return now        
        
