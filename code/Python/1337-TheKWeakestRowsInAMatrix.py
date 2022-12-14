class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        strength = [(sum(mat[i]),i) for i in xrange(len(mat))]
        strength.sort(key= lambda x: (x[0],x[1]))
        rows = map(lambda x: x[1], strength)
        return rows[:k]