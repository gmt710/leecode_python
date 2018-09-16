class Solution(object):
    def Sort(self, str_s):
        """
        :type strs: str
        :rtype: str
        """
        str_ss = list(str_s)
        str_ss.sort()
        return ''.join(str_ss)
    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        m = defaultdict(lambda : None)
        
        for s in strs:
            ss = self.Sort(s)
            if m[ss]:
                m[ss].append(s)
            else:
                m[ss] = [s]
        
        ans = []
        for k in m:
            ans.append(m[k])
        return ans
            
        
