class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smaller = []
        for i in xrange(len(nums)):
            crn_cnt = 0
            for j in xrange(len(nums)):
                if i != j and nums[j] < nums[i]:
                    crn_cnt += 1
            smaller.append(crn_cnt)
        return smaller