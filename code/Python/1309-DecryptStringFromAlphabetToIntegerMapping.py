class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        hs1 = {}
        hs2 = {}
        for i in xrange(1,10):
            hs1[str(i)] = chr(i+96)
        for i in xrange(10,27):
            hs2[str(i)+'#'] = chr(i+96)

        for key in hs2:
            s = s.replace(key, hs2[key])
        for key in hs1:
            s = s.replace(key, hs1[key])
        return s