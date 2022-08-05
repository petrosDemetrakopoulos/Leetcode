class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        already_in = []
        for i in xrange(len(nums)+1):
            already_in.append(i)
        return list(set(already_in) - set(nums))[0]