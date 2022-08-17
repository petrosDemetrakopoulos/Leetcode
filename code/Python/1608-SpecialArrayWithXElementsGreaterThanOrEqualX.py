class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for x in xrange(max(nums)+1):
            cnt = 0
            for i in xrange(len(nums)):
                if nums[i] >= x:
                    cnt += 1
            if cnt == x:
                return x
        return -1