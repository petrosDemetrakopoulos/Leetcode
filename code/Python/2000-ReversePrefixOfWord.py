class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        index = word.find(ch)
        list_word = list(word)
        reversed_prefix = "".join(list_word[:index+1])[::-1]
        return reversed_prefix + word[index+1:]