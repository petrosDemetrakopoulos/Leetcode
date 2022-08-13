class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        i = len(words) -1
        while i > 0:
            if sorted(list(words[i])) == sorted(list(words[i-1])):
                del words[i]
                i = len(words) -1
            else:
                i = i - 1
        return words