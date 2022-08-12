from itertools import combinations
class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subs = []
        for i in xrange(1,len(nums)+1):
            subs.append(map(lambda x: list(x), combinations(nums,i)))
        subs = reduce(lambda x,y: x+y, subs)
        xors = map(lambda x: reduce(lambda i, j: int(i) ^ int(j), x), subs)
        return sum(xors)