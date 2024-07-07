class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        
        maxProduct = nums[0]
        minProduct = nums[0]
        result = nums[0]

        for i in range(1,len(nums)):
            current = nums[i]
            if current < 0:
                temp = maxProduct
                maxProduct = minProduct
                minProduct = temp

            maxProduct = max(current, maxProduct * current)
            minProduct = min(current, minProduct * current)
            result = max(result, maxProduct)
        return result