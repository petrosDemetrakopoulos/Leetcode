class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos = []
        neg = []
        res = []
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        
        neg_index = 0
        pos_index = 0
        for i in xrange(len(nums)):
            if i % 2 == 0:
                res.append(pos[pos_index])
                pos_index += 1
            else:
                res.append(neg[neg_index])
                neg_index += 1
        return res