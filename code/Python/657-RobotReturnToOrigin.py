class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x = 0
        y = 0
        for m in moves:
            if m == 'R':
                x += 1
            if m == 'L':
                x -= 1
            if m == 'U':
                y += 1
            if m == 'D':
                y -= 1
        return x == 0 and y == 0