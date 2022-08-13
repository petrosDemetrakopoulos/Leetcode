class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        res = []
        for i in xrange(len(nums)):
            for j in xrange(len(nums)):
                if abs(i - j) <= k and nums[j] == key:
                    res.append(i)
        res = list(set(res))
        res.sort()
        return res