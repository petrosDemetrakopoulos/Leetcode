class Solution(object):
    def replaceDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = list(s)
        for i in range(1,len(s),2):
            ascii_c = ord(list_s[i-1])
            list_s[i] = chr(ascii_c + int(list_s[i]))
        return "".join(list_s)