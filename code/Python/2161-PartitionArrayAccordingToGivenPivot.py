class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        res = []
        for i in nums:
            if i < pivot:
                res.append(i)
        for i in nums:
            if i == pivot:
                res.append(i)
        for i in nums:
            if i > pivot:
                res.append(i)
        return res