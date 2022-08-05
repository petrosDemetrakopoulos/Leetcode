class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_s = s.split("|")
        res = 0
        for i in xrange(len(list_s),2):
            for j in list_s[i]:
                if j == '*':
                    res += 1
        return res