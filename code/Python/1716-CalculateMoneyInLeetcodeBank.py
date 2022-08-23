class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        amount = 1
        initial = 1
        cnt = 0
        for i in xrange(n):
            if cnt == 7:
                amount = initial + 1
                initial += 1
                cnt = 0
            cnt += 1
            res += amount
            amount += 1
        return res