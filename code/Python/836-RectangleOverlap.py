class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if (rec2[1] >= rec1[3] or rec2[0]>=rec1[2] or rec2[3]<=rec1[1] or rec1[0]>=rec2[2]):
            return False
        else:
            return True