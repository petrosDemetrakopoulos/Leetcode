class Solution(object):
    def checkXMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        points_in_d = []
        for i in xrange(len(grid)):
            if grid[i][i] == 0:
                return False
            points_in_d.append([i,i])

        for i in xrange(len(grid),0,-1):
            if grid[len(grid) - i][i-1] == 0:
                return False
            points_in_d.append([len(grid) - i,i-1])
        
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if [i,j] not in points_in_d:
                    if grid[i][j] != 0:
                        return False
        return True