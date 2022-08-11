class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2:
            return True
        cnt = 0
        for i in xrange(len(s1)):
            if s1[i] != s2[i]:
                if s1.count(s1[i]) != s2.count(s1[i]):
                    return False
                cnt += 1 
        if cnt > 2:
            return False
        else:
            return True