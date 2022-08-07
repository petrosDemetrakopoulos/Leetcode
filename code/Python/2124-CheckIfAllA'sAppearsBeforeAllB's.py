class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b_found = False
        for char in s:
            if char == 'b':
                b_found = True
            if char == 'a' and b_found:
                return False
        return True