class Solution(object):
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        l_sentence = sentence.split()
        for i in xrange(len(l_sentence)):
            for j in dictionary:
                if l_sentence[i].startswith(j):
                    l_sentence[i] = j
        return " ".join(l_sentence)