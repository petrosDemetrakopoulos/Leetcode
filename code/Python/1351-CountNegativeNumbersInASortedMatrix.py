class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i]) -1, -1, -1):
                if grid[i][j] < 0:
                    res += 1
                else:
                    break
        return res