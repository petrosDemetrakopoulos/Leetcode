class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        if len(nums) == 1:
            nums[0].sort()
            return nums[0]
        res = [value for value in nums[0] if value in nums[1]]
        for i in range(1,len(nums)):
            res = [value for value in res if value in nums[i]]
        res.sort()
        return res