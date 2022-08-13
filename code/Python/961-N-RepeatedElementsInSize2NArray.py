class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 2
        for i in range(2*n):
            nums_rep = 1
            for j in range(2*n):
                if i != j:
                    if nums[i] == nums[j]:
                        nums_rep += 1
                        if nums_rep == n:
                            return nums[i]