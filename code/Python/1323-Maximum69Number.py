class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num))
        i = 0
        while  i < len(digits) and digits[i] == '9':
            i += 1
        if i < len(digits):
            digits[i] = '9'
        return int("".join(digits))