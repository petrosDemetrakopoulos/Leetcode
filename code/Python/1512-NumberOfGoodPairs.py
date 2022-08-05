class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for i in xrange(len(nums)):
            for j in xrange(i):
                cnt += 1 if nums[i] == nums[j] else 0
        return cnt