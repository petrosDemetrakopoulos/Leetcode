class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        reversed_s = list(s)
        for i in xrange(len(indices)):
            reversed_s[indices[i]] = s[i]
        return "".join(reversed_s)