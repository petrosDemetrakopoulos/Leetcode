class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        crn_max = ''
        for i in s:
            if i.swapcase() in s:
                crn_max = max(crn_max,i.upper())
        return crn_max