class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        while part in s:
            part_find = s.find(part)
            if part_find != -1:
                s = s[0:part_find] + s[part_find+len(part):len(s)]
        return s