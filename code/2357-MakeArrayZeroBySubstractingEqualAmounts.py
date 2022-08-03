class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) == 0:
            return 0
        ops = 0
        only_pos = list(filter(lambda x: x > 0, nums))
        sub_by = min(only_pos)
        while (sum(nums) > 0):
            for i in range(len(nums)):
                if nums[i] >= sub_by:
                    nums[i] = nums[i] - sub_by
            ops += 1
            if sum(nums) > 0:
                only_pos = list(filter(lambda x: x > 0, nums))
                sub_by = min(only_pos)
        return ops