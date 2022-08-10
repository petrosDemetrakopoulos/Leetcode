# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        left = 1
        right = n
        res = -1
        while res != 0:
            mid = (left + right) /2
            res = guess(mid)
            if res == -1:
                right = mid - 1
            elif res == 1:
                left = mid + 1
            else:
                return mid