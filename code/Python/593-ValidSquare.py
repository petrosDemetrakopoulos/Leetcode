class Solution(object):
    def dist(self,p1,p2):
        return (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        distances = set()
        distances.add(self.dist(p1,p2))
        distances.add(self.dist(p2,p3))
        distances.add(self.dist(p3,p4))
        distances.add(self.dist(p1,p3))
        distances.add(self.dist(p1,p4))
        distances.add(self.dist(p2,p4))
        
        # sides should be equal and diagonals should be equals, so only 2 distinct distances should exist in the set
        return len(distances) == 2 and 0 not in distances