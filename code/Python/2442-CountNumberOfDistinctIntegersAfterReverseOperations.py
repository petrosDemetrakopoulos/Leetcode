class Solution(object):
    def countDistinctIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        revs = []
        for num in nums:
            rev = str(num)[::-1]
            revs.append(int(rev))
        nums = nums + revs
        return len(set(nums))