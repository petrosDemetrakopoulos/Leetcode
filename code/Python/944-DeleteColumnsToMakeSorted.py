class Solution(object):
    def minDeletionSize(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        res = 0
        transposed = zip(*strs)
        for col in xrange(len(transposed)):
            for char in xrange(len(transposed[col])-1):
                if transposed[col][char+1] < transposed[col][char]:
                    res += 1
                    break
        return res