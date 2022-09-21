from collections import Counter
class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = sorted(Counter(nums).most_common(), key=lambda x: (-x[1],x[0]))
        for pair in freq:
            if pair[0] % 2 == 0:
                return pair[0]
        return -1