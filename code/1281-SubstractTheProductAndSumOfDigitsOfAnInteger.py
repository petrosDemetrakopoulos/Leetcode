class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = [int(a) for a in str(n)]
        prod = reduce((lambda x, y: x * y), digits)
        summ = sum(digits)
        return prod - summ