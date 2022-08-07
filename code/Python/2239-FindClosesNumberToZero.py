class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        abs_vals = list(map(lambda x: abs(x), nums))
        
        min_abs =  min(abs_vals)
        if min_abs in nums:
            return min_abs
        else:
            return -1*min_abs