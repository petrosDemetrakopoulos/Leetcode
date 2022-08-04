class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        prim_diag = []
        sec_diag = []
        j = 0
        for i in xrange(len(mat)):
            prim_diag.append([i,j])
            sec_diag.append([i,len(mat) - j -1])
            j += 1
        all_diag = prim_diag + sec_diag
        all_diag_set = list(set(tuple(row) for row in all_diag))
        all_diag_val = list(map(lambda x: mat[x[0]][x[1]],all_diag_set))
        return sum(all_diag_val)
            