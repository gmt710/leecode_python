class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        map_table = {'2':"abc",'3':"def",
                     '4':"ghi",'5':"jkl",'6':"mno",
                    '7':"pqrs",'8':"tuv",'9':"wxyz"}
        if not digits:
            return []

        res = [i for i in map_table[digits[0]]]
        for i_digit in digits[1:]:
            # 可以根据digits中数字的个数不断扩展
            res = [m+n for m in res for n in map_table[i_digit]]
        return res
                    
            
                
                
