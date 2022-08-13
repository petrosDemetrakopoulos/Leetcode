class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        subs_set = set()
        for i in xrange(len(s)-k+1):
            subs_set.add(s[i:i+k])
        if len(subs_set) == 2**k:
            return True
        return False