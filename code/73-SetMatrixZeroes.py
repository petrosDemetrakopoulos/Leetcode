class Solution(object):
    zeroed = {}
    def zeroRow(self, row, matrix):
        for i in xrange(0,len(matrix[row])):
            if matrix[row][i] != 0:
                matrix[row][i] = 0
                self.zeroed[row][i] = True

    def zeroCol(self, col, matrix):
        for i in xrange(len(matrix)):
            if matrix[i][col] != 0:
                matrix[i][col] = 0
                self.zeroed[i][col] = True
        
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        for i in xrange(len(matrix)):
            self.zeroed[i] = {}
            for j in xrange(len(matrix[i])):
                self.zeroed[i][j] = False

        for i in xrange(len(matrix)):
            row = matrix[i]
            for j in xrange(len(row)):
                if matrix[i][j] == 0 and self.zeroed[i][j] == False:
                    self.zeroRow(i,matrix)
                    self.zeroCol(j, matrix)