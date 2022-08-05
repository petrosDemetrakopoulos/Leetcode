class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = 3
        for i in xrange(200):
            if res == n:
                return True
            res = 3**i
        return False