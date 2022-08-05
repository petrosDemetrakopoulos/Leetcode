class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 1:
            return [[1]]
        
        sol = [[1],[1,1]]
        for i in xrange(2, numRows):
            previousRow = i -1
            crnRow = [1]
            for j in xrange(len(sol[previousRow]) - 1):
                sum_to_add = sol[previousRow][j] + sol[previousRow][j+1]
                crnRow.append(sum_to_add)
            crnRow.append(1)
            sol.append(crnRow)
        return sol