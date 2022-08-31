from collections import Counter
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hs = sorted(Counter(nums).most_common(), key=lambda x: (x[1],-x[0]))
        res = []
        for i in xrange(len(hs)):
            res += [hs[i][0] for x in xrange(hs[i][1])]
        return res