class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sums = []
        for i in xrange(len(nums)):
            crnSum = nums[0]
            for j in xrange(1,i + 1):
                crnSum += nums[j]
            sums.append(crnSum)
        return sums