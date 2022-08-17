class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        flattened = [item for sublist in matrix for item in sublist]
        flattened.sort()
        return flattened[k-1]