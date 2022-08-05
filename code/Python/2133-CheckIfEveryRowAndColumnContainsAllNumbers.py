class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        transposed = zip(*matrix)
        rng = list(range(1, len(matrix) + 1))
        transposed = list(map(lambda x: list(x), transposed))
        for i in xrange(len(matrix)):
            crn_ln = matrix[i]
            crn_ln.sort()
            if crn_ln != rng:
                return False
            crn_transposed = transposed[i]
            crn_transposed.sort()
            if crn_transposed != rng:
                return False
        return True