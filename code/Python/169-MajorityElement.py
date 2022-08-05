class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        majority = -1
        max = 0
        for i in nums:
            if i not in hash_table:
                hash_table[i] = 1
            else:
                hash_table[i] += 1
            if hash_table[i] >= max:
                max = hash_table[i]
                majority = i
        return majority