class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        negative = 0
        if numerator * denominator < 0:
            negative = 1
        numerator, denominator = abs(numerator), abs(denominator)

        answer = []
        answer.append(str(numerator/denominator))
        remainder = numerator % denominator
        if remainder:
            answer.append(".")
        # Keep the start position of the repeating part
        remainder_start = {}
        while remainder:
            remainder *= 10
            if remainder in remainder_start:
                # 插入到余数相同的answer位置处
                answer.insert(remainder_start[remainder], "(")
                answer.append(")")
                break
            else:
                # 记录余数相同的answer位置
                remainder_start[remainder] = len(answer)
                answer.append(str(remainder/denominator))
                remainder = remainder % denominator
                
        if negative:
            answer.insert(0, "-")
            return "".join(answer)
        else:
            return "".join(answer)

        
