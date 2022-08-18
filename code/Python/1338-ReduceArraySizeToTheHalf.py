from collections import Counter
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        hs = Counter(arr).most_common()
        res = 0
        cnt = 0
        for x in hs:
            cnt += x[1]
            res += 1
            if cnt >= (len(arr) / 2):
                return res
        return res