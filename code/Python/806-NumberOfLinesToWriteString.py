class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        alphabet = string.ascii_lowercase
        hs = {}
        for letter in range(len(alphabet)):
            hs[alphabet[letter]] = widths[letter]
        
        lines = 0
        crn_line = 0
        for c in s:
            crn_line += hs[c]
            if crn_line > 100:
                lines += 1
                crn_line = hs[c]
        lines += 1 if crn_line > 0 else 0
        return [lines, crn_line]