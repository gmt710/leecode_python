class Solution(object):
    result_list = []
    def generate(self, s, n):
        # 回溯中每次遍历字符串s寻找右括号，
        # 若右括号在位置i，在此之前的字符串左括号数大于右括号数，
        # 且前一个字符为左括号，则与前一字符交换。
            global result_list
            new_s = s
            left = right = 0
            for i in range(n * 2):
                if s[i] == '(':
                    left += 1
                else:
                    right += 1
                    if left > right and s[i - 1] == '(':
                        new_s = s[:i - 1] + s[i:i + 1] + s[i - 1:i] + s[i + 1:]
                        if new_s not in result_list:
                            result_list += [new_s]
                            self.generate(new_s, n)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        global result_list 
        s = '(' * n + ')' * n
        result_list = [s]
        self.generate(s, n)
        return result_list
        
        # 超出时间限制
#         res = []
#         self.generate(n, n, "", res)
#         return res
    
#     def generate(self, left, right, Str, res):
#         # 如果左括号还有剩余，则可以放置左括号，如果右括号的剩余数大于左括号，则可以放置右括号。
#         if left == 0 and right == 0:
#             res.append(Str)
#             print(res)
#             return
#         # 如果左括号的个数还有剩余，则+’(‘然后递归
#         if left > 0:
#             self.generate(left-1, right, Str+'(', res)
#         # 如果右括号有剩余且小于左括号的个数则+‘)’
#         if right > left:
#             self.generate(left, right-1, Str+')', res)
        
