class Solution(object):
    def isStrictlyIncreasing(self,nums):
        for i in xrange(len(nums) - 1):
            if nums[i+1] <= nums[i]:
                return False
        return True

    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if self.isStrictlyIncreasing(nums):
            return True
        for i in xrange(len(nums) - 1):
            if nums[i+1] <= nums[i]:
                if self.isStrictlyIncreasing(nums[:i+1] + nums[i+2:]) or self.isStrictlyIncreasing(nums[:i] + nums[i+1:]):
                    return True
        return False