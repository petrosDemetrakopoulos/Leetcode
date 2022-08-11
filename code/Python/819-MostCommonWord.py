class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragrpah_list = paragraph.replace(',',' ').replace('.','').replace('!','').replace('?','').replace(';','').replace('\'','').lower().split()
        hs = {}
        for word in paragrpah_list:
            if word not in hs and word not in banned:
                hs[word] = paragrpah_list.count(word)

        max_freq = 0
        common_word = ''
        for i in range(len(hs.values())):
            if hs.values()[i] > max_freq:
                max_freq = hs.values()[i]
                common_word = hs.keys()[i]
        return common_word
            