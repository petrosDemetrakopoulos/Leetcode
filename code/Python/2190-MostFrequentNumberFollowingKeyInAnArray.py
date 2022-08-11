class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        hs = {}
        for i in xrange(len(nums)-1):
            if nums[i] == key:
                if nums[i+1] not in hs:
                    hs[nums[i+1]] = 1
                else:
                    hs[nums[i+1]] += 1
        max_val = 0
        max_key = -1
        for i in xrange(len(hs.values())):
            if hs.values()[i] > max_val:
                max_val = hs.values()[i]
                max_key = hs.keys()[i]
        return max_key