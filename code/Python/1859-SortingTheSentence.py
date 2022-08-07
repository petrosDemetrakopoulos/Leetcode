class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        list_s = s.split()
        res = ['' for x in list_s]
        for word in list_s:
            word_num = int(word[len(word) - 1:])
            res[word_num - 1] = word[:len(word)-1]
        return " ".join(res)