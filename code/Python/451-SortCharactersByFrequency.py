from collections import Counter
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = Counter(s).most_common()
        res = ''
        for i in freq:
            res += i[0]* i[1]
        return res