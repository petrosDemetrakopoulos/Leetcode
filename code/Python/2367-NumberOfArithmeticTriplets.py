class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        cnt = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        cnt += 1
        return cnt