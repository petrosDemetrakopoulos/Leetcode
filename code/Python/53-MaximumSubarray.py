class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSub = nums[0]
        crnSum = 0
        
        for i in nums:
            if crnSum < 0:
                crnSum = 0
            crnSum += i
            maxSub = max(maxSub, crnSum)
        return maxSub