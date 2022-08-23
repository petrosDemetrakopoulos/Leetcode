class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums) == len(nums) and k==0:
            return True
        places = []
        for i in xrange(len(nums)):
            if nums[i] == 1:
                places.append(i)
        for i in xrange(len(places)):
            for j in xrange(len(places)):
                if i != j:
                    if abs(places[i] - places[j]) <= k:
                        return False
        return True
            