class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        seen = []
        for i in s:
            if i not in seen:
                seen.append(i)
            else:
                return i