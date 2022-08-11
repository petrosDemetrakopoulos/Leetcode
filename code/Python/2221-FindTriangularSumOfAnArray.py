class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        while len(nums) > 1:
            newNums = []
            for i in xrange(len(nums)-1):
                newNums.append((nums[i] + nums[i+1]) % 10)
            nums = newNums
        return nums[0]