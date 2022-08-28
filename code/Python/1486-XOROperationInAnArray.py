class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums = [start + 2 * i for i in xrange(n)]
        return reduce(lambda x, y: x ^ y, nums)