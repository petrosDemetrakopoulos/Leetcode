class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        d = reduce(lambda a,b: a+b,[list(str(x)) for x in nums])
        d = reduce(lambda a,b: a+b, [int(x) for x in d])
        return abs(s-d)