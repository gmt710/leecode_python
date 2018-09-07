class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices)<2:
            return 0
        result = 0
        
        Begin_value = prices[0]
        for p in prices:
            if p > Begin_value:
                result += p - Begin_value
                Begin_value = p
            else:
                Begin_value = min(p, Begin_value)
        
        return result
        
