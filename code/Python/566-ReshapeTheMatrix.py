class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        res = []
        new_row = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                new_row.append(mat[i][j])
                if len(new_row) == c:
                    res.append(new_row)
                    new_row = []
        return res