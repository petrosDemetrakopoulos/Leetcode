class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        s_list = sentence.split()
        for i in xrange(len(s_list)):
            if s_list[i].startswith(searchWord):
                return i+1
        return -1