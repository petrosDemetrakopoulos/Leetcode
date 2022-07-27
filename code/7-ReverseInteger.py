class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x > 0 else -1
        res = 0  
        if sign == -1:
            x = -x
        while (x > 0):  
            remainder = x % 10  
            res = (res * 10) + remainder  
            x = x // 10  
        result = res*sign
        if result > (2**31 - 1) or result < (-2**31):
            return 0
        else:
            return result