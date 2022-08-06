class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        s1 = "".join(list(reduce(lambda x,y: x + y, word1)))
        s2 = "".join(list(reduce(lambda x,y: x + y, word2)))
        return s1 == s2