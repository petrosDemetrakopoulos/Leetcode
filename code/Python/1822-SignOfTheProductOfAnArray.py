class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 in nums:
            return 0
        prod = 1
        for i in nums:
            prod = prod*i
        return 1 if prod > 0 else -1