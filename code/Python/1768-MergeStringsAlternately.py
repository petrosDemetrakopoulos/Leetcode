class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ''
        list_1 = list(word1)
        list_2 = list(word2)
        cnt_1 = 0
        cnt_2 = 0
        for i in xrange(len(list_1) + len(list_2)):
            if i % 2 == 0 and cnt_1 < len(list_1) or (cnt_2 >= len(list_2)):
                res += list_1[cnt_1]
                cnt_1 += 1
            elif i % 2 == 1 and cnt_2 < len(list_2) or (cnt_1 >= len(list_1)):
                res += list_2[cnt_2]
                cnt_2 += 1
        return res