class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        res = 0
        transposed = zip(*mat)
        for row in xrange(len(mat)):
            for col in xrange(len(mat[row])):
                if mat[row][col] == 1:
                    if sum(mat[row]) == 1 and sum(transposed[col]) == 1:
                        res += 1
        return res