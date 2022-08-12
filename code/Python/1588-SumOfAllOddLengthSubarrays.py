from itertools import combinations
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        tot = 0
        for i in range(len(arr)):
            left = i + 1
            right = len(arr) - i
            num_subs = left * right
            odd_subs = num_subs // 2 if num_subs % 2 == 0 else (num_subs // 2) + 1
            tot += odd_subs * arr[i]
        return tot