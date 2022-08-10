class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        half = len(candyType) / 2
        len_set = len(set(candyType))
        if half <= len_set:
            return half
        else:
            return len_set