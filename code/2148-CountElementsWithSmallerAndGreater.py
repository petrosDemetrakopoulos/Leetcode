class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 0
        for i in xrange(len(nums)):
            lower = False
            greater = False
            for j in xrange(len(nums)):
                if i != j:
                    if nums[j] < nums[i]:
                        lower = True
                    elif nums[j] > nums[i]:
                        greater = True
            cnt += lower and greater
        return cnt