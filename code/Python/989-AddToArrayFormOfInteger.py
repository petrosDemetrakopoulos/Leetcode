class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        mult = 1
        integer = 0
        for i in xrange(len(num)-1,-1,-1):
            integer += num[i] * mult
            mult = mult * 10
        res = integer + k
        return list(str(res))