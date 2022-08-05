class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freqs = {}
        for i in nums:
            if i not in freqs:
                freqs[i] = 1
            else:
                freqs[i] += 1

        # sort freqs.values and freqs.keys in parallel based on freqs.values
        zipped_lists = zip(freqs.values(), freqs.keys())
        sorted_pairs = sorted(zipped_lists, reverse=True)

        tuples = zip(*sorted_pairs)
        sorted_values, sorted_keys = [list(tuple) for tuple in  tuples]
        return sorted_keys[:k]