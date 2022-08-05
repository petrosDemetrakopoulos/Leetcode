class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = s.split()
        for i in xrange(len(list_s)):
            list_s[i] = list_s[i][::-1]
        return " ".join(list_s)