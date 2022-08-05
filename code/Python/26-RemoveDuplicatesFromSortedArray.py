class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        for i in nums[1:]:
            if i not in nums[:k]:
                k += 1
            else:
                nums.append(nums.pop(k))
        return k