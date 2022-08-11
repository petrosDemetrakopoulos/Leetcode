class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hs = {}
        for i in nums:
            if i not in hs:
                hs[i] = nums.count(i)
        
        res = 0
        for i in range(len(hs.values())):
            if hs.values()[i] == 1:
                res += hs.keys()[i]
        return res