class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res = 0
        for i in xrange(len(nums)):
            for j in xrange(i,len(nums)):
                if i!= j:
                    if nums[i] == nums[j] and (i*j) % k == 0:
                        res += 1
        return res