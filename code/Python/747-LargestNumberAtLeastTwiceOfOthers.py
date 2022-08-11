class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        max_index = -1
        for i in xrange(len(nums)):
            if nums[i] != max_num:
                if 2*nums[i] > max_num:
                    return -1
            else:
                max_index = i
        return max_index