class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
            res.append(i)
        for i in nums:
            res.append(i)
        return res