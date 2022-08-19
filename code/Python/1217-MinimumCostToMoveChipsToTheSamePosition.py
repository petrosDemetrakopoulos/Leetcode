class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        evens = len(filter(lambda x: x % 2 == 0, position))
        odds = len(filter(lambda x: x % 2 == 1, position))
        
        return min(evens,odds)  