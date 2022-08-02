class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n in [1,2]:
            return 1
        temp_tbl = [0,1,1]
        for i in xrange(2,n):
            temp_tbl.append(temp_tbl[i] + temp_tbl[i-1] + temp_tbl[i-2])
        return temp_tbl[len(temp_tbl) - 1]