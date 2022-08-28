import itertools
class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        pairs = [[nums[i],nums[i+1]] for i in xrange(0,len(nums),2)]
        
        for p in pairs:
            freq = p[0]
            val = p[1]
            ls = [val for i in xrange(freq)]
            res.append(ls)
        return list(itertools.chain(*res))
                
            