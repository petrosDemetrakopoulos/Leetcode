class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = n
        while res % 2 != 0 or res % n != 0:
            res += 1
        return res