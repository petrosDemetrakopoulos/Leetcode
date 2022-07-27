class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #for lines
        for i in xrange(len(board)):
            uniques_per_line = []
            for j in xrange(0,len(board[i])):
                if (board[i][j] != '.'):
                    if (board[i][j] in uniques_per_line or
                int(board[i][j]) > 9 or int(board[i][j]) < 1):
                        return False
                    else:
                        uniques_per_line.append(board[i][j])
        # for columns
        transposed = list(zip(*board))
        transposed = list(map(lambda x: list(x), transposed))

        for i in xrange(len(transposed)):
            uniques_per_col = []
            for j in xrange(len(transposed[i])):
                if (transposed[i][j] != '.'):
                    if (transposed[i][j] in uniques_per_col or
                int(transposed[i][j]) > 9 or int(transposed[i][j]) < 1):
                        return False
                    else:
                        uniques_per_col.append(transposed[i][j])
        
        squares = []
        crn_ln = 0
        k = 1
        startCol = 0
        for big in xrange(0,9):
            crn_sq = []
            if big in [3,6]:
                startCol = 0
                
            if big <= 2:
                for i in xrange(3): # 0 = 2-2
                    for j in xrange(startCol,startCol + 3):
                        if board[i][j] != '.':
                            crn_sq.append(board[i][j])
            elif big <= 5:
                for i in xrange(3,6): # 3 = 5 -2
                    for j in xrange(startCol,startCol + 3):
                        if board[i][j] != '.':
                            crn_sq.append(board[i][j])
            elif big <= 8:
                for i in xrange(6,9):# 6 = 8 -2
                    for j in xrange(startCol,startCol + 3):
                        if board[i][j] != '.':
                            crn_sq.append(board[i][j])
                
            startCol += 3
            squares.append(crn_sq)

        for i in xrange(len(squares)):
            uniques_per_square = []
            for j in xrange(len(squares[i])):
                if squares[i][j] not in uniques_per_square:
                    uniques_per_square.append(squares[i][j])
                else:
                    return False
    
        return True