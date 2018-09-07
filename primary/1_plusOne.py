class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit = 0
        for i in range(len(digits)):
            digit = 10 * digit + digits[i]    
        digit = digit + 1
        digits = []
        while (digit):
            k = digit % 10
            digit = digit / 10
            digits.insert(0,k)
        return digits
