class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 9:
            return num
        temp = num
        mod = 0
        while temp >= 10:
            new = temp // 10
            mod = temp % 10
            temp = new + mod
        return temp