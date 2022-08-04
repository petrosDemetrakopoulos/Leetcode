class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = 0
        for i in xrange(len(nums)):
            for j in xrange(i, len(nums)):
                if i != j:
                    cnt += 1 if abs(nums[i] - nums[j]) == k else 0
        return cnt
                    