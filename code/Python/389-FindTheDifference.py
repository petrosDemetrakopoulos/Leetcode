class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in xrange(len(s)):
            t = t.replace(s[i],"",1)
        return t