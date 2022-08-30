import math
class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n > 0 and 4**int(math.log(n, 4)) == n)