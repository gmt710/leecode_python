class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        
        len_min = min([len(x) for x in strs])
        i = 0 
        while i < len_min:
            for j in range(len(strs)):
                if strs[j][i] != strs[j-1][i]:
                    return strs[0][:i]
            i += 1
        return strs[0][:i]

#         if not strs:
#             return ""
#         if len(strs) == 1:
#             return strs[0]
#         minl = min([len(x) for x in strs])
#         end = 0
#         while end < minl:
#             for i in range(1,len(strs)):
#                 if strs[i][end]!= strs[i-1][end]:
#                     return strs[0][:end]
#             end += 1
#         return strs[0][:end]
