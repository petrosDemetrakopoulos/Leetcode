class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for i in range(len(nums)):
	        if len(list(str(nums[i]))) % 2 == 0:
		        cnt += 1
        return cnt