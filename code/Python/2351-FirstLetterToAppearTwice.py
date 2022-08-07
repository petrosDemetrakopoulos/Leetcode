class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        hm = {}
        for i in s:
            if i not in hm:
                hm[i] = 1
            else:
                return i