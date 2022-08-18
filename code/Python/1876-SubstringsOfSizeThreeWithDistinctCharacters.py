class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in xrange(len(s)-2):
            if len(set(s[i:i+3])) == 3:
                res += 1
        return res