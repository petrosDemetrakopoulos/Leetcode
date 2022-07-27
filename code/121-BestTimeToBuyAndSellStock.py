class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        max_price = 0
        min_price = 10 ** 4
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] > max_price:
                max_price = max(max_price, prices[i] - min_price)
        return max_price