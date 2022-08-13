class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        list_s = s.split()
        list_s.reverse()
        return " ".join(list_s)