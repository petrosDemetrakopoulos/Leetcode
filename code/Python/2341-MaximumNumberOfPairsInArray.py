class Solution(object):
    def numberOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        res = [0,0]
        for i in nums:
            freq[i] = nums.count(i)
            
        for i in freq.values():
            res[0] += i//2
            res[1] += i % 2
        return res