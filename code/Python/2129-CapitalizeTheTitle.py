class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        words = title.split()
        for i in xrange(len(words)):
            words[i] = words[i].lower()
            if (len(words[i]) not in [1,2]):
                words[i] = words[i][:0] + words[i][0].upper() + words[i][1:]
        return " ".join(words)