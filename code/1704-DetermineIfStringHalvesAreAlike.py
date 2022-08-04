class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        va = 0
        vb = 0
        for i in xrange(len(a)):
            va += 1 if a[i] in vowels else 0
            vb += 1 if b[i] in vowels else 0
        return va == vb