class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x in [0,1]):
            return x
        i = 1
        result = 1
        while (result <= x):
            i += 1
            result = i * i
        return i - 1