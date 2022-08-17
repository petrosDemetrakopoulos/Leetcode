class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        tot = 0
        cols = list(map(lambda x: list(x), zip(*grid)))
        for i in grid:
            for j in cols:
                if i == j:
                    tot += 1
        return tot