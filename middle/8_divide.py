class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 如果除数与被除数符号不同的话，返回的符号为-1，否则为1
        flag = -1 if (dividend<0) ^ (divisor<0) else 1
        
        # 如果除数大于被除数，则不够除
        if abs(divisor) > abs(dividend) :
            return 0
        # 只有当除数为+/-1时，结果才会存在溢出的现象
        if abs(divisor) == 1:
            return 2**31-1 if flag*abs(dividend) >= 2**31-1 else flag*abs(dividend)
        # 由除数到被除数之间有多少个除数，来计算商
        return flag * len(xrange(abs(divisor),abs(dividend)+1,abs(divisor)))

    
