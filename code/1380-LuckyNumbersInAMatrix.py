class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        cols = zip(*matrix)
        res = []
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                if matrix[i][j] == min(matrix[i]):
                    if matrix[i][j] == max(cols[j]):
                        res.append(matrix[i][j])
        return res