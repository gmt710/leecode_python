class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        num1 = []
        str_x = str(x)
        if str_x[0] == '-':
            num1 = str_x[1:][::-1]
            num = int(num1)
            if num>2**31:
                return 0
            return -num
        else:
            num1 = str_x[::-1]
            num = int(num1)
            if num > 2**31:
                return 0
            return num
    
