class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st_nums = sorted(list(set(nums)))
        print(st_nums)
        if len(st_nums) < 3:
            return st_nums[len(st_nums) - 1]
        return st_nums[len(st_nums)-3]