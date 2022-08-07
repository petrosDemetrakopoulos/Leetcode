import itertools
class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pairs = []
        res = []
        for i in xrange(0,len(nums),2):
            pairs.append([nums[i],nums[i+1]])
        
        for p in pairs:
            freq = p[0]
            val = p[1]
            ls = []
            for i in xrange(freq):
                ls.append(val)
            res.append(ls)
        return list(itertools.chain(*res))
                
            