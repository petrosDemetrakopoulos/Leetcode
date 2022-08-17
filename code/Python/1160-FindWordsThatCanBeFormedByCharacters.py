class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        res = 0
        for word in words:
            canBeFormed = True
            crn_chars = list(chars)
            for i in xrange(len(word)):
                char = word[i]
                if char not in crn_chars:
                    canBeFormed = False
                    break
                else:
                    del crn_chars[crn_chars.index(char)]
            if canBeFormed:
                res += len(word)
        return res