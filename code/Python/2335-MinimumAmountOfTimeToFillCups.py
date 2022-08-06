class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        #cold = amount[0]
        #warm = amount[1]
        #hot = amount[2]
        
        t = 0
        while amount[0] > 0 or amount[1] > 0 or amount[2] > 0:
            amount.sort(reverse=True)
            if amount[0] > 0 and amount[1] >0:
                amount[0] = amount[0] - 1
                amount[1] = amount[1] - 1
            elif amount[0] > 0:
                amount[0] = amount[0] - 1
            elif amount[1] > 0:
                amount[1] = amount[1] - 1
            elif amount[2] > 0:
                amount[2] = amount[2] -1
            t += 1
            print amount
        return t