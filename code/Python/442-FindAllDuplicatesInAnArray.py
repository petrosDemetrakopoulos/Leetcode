class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        res = []
        for i in xrange(len(nums)-1):
            if nums[i] == nums[i+1]:
                res.append(nums[i])
        return res