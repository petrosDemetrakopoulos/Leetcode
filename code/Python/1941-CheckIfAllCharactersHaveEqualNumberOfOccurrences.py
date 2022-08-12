class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        hs = {}
        for i in s:
            hs[i] = s.count(i)
        
        for i in hs.values():
            if i != hs.values()[0]:
                return False
        return True