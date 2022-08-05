class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        crn_max = 0
        for i in nums:
            if i == 0:
                if cnt > crn_max:
                    crn_max = cnt
                cnt = 0
            else:
                cnt += 1
                
        crn_max = cnt if cnt > crn_max else crn_max
        return crn_max