class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        letters = string.ascii_lowercase + string.ascii_uppercase
        lets = []
        for char in s:
            if char in letters:
                lets.append(char)
        lets.reverse()
        reversedS = ''
        i = 0
        for j in xrange(len(s)):
            char = s[j]
            if char in letters:
                reversedS += lets[i]
                i += 1
            else:
                reversedS += s[j]
        return reversedS