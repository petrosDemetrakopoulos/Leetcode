from itertools import izip_longest
class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        lst = s.split()
        lst = [list(x) for x in lst]
        transposed = list(izip_longest(*lst, fillvalue=" "))
        res = []
        for word in transposed:
            res.append(''.join(list(word)).rstrip())
        return res