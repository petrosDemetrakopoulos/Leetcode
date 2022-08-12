class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        cnt = 0
        for n in xrange(1,num+1):
            digits = [int(a) for a in str(n)]
            if sum(digits) % 2 == 0:
                cnt += 1
        return cnt