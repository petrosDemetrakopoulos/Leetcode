from collections import Counter
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        c = Counter(words)
        c = sorted(c.items(), key=lambda x: (-x[1], x[0]))[:k]
        return [x[0] for x in c]