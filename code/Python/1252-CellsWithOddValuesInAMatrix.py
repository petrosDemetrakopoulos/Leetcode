class Solution(object):
    def oddCells(self, m, n, indices):
        """
        :type m: int
        :type n: int
        :type indices: List[List[int]]
        :rtype: int
        """
        matrix = []
        for i in xrange(m):
            matrix.append([0] * n)
        
        for op in indices:
            row = op[0]
            col = op[1]
            for i in xrange(len(matrix[row])):
                matrix[row][i] += 1
            for i in xrange(len(matrix)):
                matrix[i][col] += 1
        odd = 0
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] % 2 == 1:
                    odd += 1
        return odd