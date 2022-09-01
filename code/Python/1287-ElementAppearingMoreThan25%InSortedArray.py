from collections import Counter
class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        freq = Counter(arr).most_common()
        for f in freq:
            if f[1] > len(arr)/4:
                return f[0]