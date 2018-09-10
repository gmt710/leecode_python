class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or prices == sorted(prices, reverse=True):
            return 0
        
        buy_price = prices[0]
        profits = 0
        for p in prices:
            profits = max(profits, p-buy_price)
            buy_price = min(buy_price, p)
        return profits
