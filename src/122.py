class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i, price in enumerate(prices[1:]):
            temp = price - prices[i]
            if temp > 0:
                profit += temp

        return profit
