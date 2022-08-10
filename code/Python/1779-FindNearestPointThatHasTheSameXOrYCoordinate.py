class Solution(object):
    def manhattanDist(self,x1,x2,y1,y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        min_dist = sys.maxint
        min_index = len(points) - 1
        for i in xrange(len(points)):
            crn_point = points[i]
            if crn_point[0] == x or crn_point[1] == y:
                dist = self.manhattanDist(x, crn_point[0], y, crn_point[1])
                if dist < min_dist:
                    min_dist = dist
                    min_index = i
        if min_dist != sys.maxint:
            return min_index
        else:
            return -1