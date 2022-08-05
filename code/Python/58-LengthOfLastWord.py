class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_str = str(s).strip().split()
        return len(list_str[len(list_str)-1])