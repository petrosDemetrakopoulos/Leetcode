class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        evens = filter(lambda x: x % 2 == 0,nums)
        odds = filter(lambda x: x % 2 == 1,nums)
        res = []
        j = 0
        k = 0
        for i in xrange(len(nums)):
            if i % 2 == 0:
                res.append(evens[j])
                j += 1
            else:
                res.append(odds[k])
                k+=1
        return res
                