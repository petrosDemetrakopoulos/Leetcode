class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        res = []
        for i in xrange(len(prices)):
            new_price = -1
            for j in xrange(i+1,len(prices)):
                if prices[j] <= prices[i]:
                    new_price = prices[i] - prices[j]
                    break
            if new_price == -1:
                res.append(prices[i])
            else:
                res.append(new_price)
        return res