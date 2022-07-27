class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sol = []
        for i in xrange(len(nums)):
            for j in xrange(len(nums)-1,0,-1):
                if i != j:
                    if (nums[i] + nums[j]) == target:
                        sol.append(i)
                        sol.append(j)
                        return sol