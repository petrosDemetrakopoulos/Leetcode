class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freqs = {}
        for i in arr:
            if i not in freqs:
                freqs[i] = arr.count(i)
        return len(set(freqs.values())) == len(freqs.values())