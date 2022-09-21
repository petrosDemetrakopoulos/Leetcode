class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        nums_len = len(nums)
        return nums[nums_len-1] * nums[nums_len -2] - nums[0]*nums[1]