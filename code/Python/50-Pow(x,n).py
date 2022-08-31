class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1
        if n > 0:
            while (n > 0):
                if (n % 2 == 0):
                    x = x * x
                    n = n / 2
                else:
                    result = result * x
                    n = n - 1
            return result
        else:
            n = -n
            while (n > 0):
                if (n % 2 == 0):
                    x = x * x
                    n = n / 2
                else:
                    result = result * x
                    n = n - 1
            return 1/result