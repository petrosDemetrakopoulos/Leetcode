class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        distincts = list(set(nums))
        sum_dist = sum(distincts)
        sum_nums = sum(nums)
        size_diff = len(nums) - len(distincts)
        return (sum_nums - sum_dist) / size_diff