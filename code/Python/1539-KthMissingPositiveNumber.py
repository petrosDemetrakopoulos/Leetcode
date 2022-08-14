class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        crn = k
        for i in arr:
            if i <= crn:
                crn += 1
        return crn