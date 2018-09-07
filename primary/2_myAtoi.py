class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        # num = 0
        # s = list(filter(str.isdigit, str(s)))
        # print(s)
        # for i in range(len(s)):
        #     num = num*10 + int(s[i])
        # return num
        
        import re
        #正则化中^代表用^后面的开头，[-+]?表示[-+]可以出现，
        # 也可以不出现，\d匹配所有数字，\d+数字后面可以连接
        # 无数数字，但不能是其他东西，包括空格和字母
        list_s = re.findall(r"^[-+]?\d+", s.strip())
        if not list_s: 
            return 0  #字母开始列表是空的,直接返回0
        else:
            num =int(''.join(list_s)) #列表转化为字符串，然后转化为整数
            if num >2**31 -1:
                return 2**31 -1
            elif num < -2**31:
                return -2**31
            else:
                return num
        
