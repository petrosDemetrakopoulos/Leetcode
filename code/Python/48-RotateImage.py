class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        cols = []
        for i in xrange(len(matrix)-1,0,-1):
            crn_col = []
            for j in xrange(len(matrix[i])):
                crn_col.append(matrix[i][j])
            cols.append(crn_col)
        cols.append(matrix[0])
        tbl = list(map(lambda x: list(x), list(zip(*cols))))
        for i in xrange(len(tbl)):
            matrix[i] = tbl[i]