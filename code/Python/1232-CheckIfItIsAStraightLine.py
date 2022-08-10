class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x1 = coordinates[0][0]
        x2 = coordinates[1][0]
        y1 = coordinates[0][1]
        y2 = coordinates[1][1]
        
        if x1 == x2:
            res = False
            for i in xrange(len(coordinates)):
                crn_x = coordinates[i][0]
                if crn_x != x1:
                    return False
            return True
        
        a = float(y1 - y2)/float(x1-x2)
        b = y1 - a * x1

        for i in xrange(2, len(coordinates)):
            crn_y = coordinates[i][1]
            crn_x = coordinates[i][0]
            if crn_y != a * crn_x + b:
                return False
        return True