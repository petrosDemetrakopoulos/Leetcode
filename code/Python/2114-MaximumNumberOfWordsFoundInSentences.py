class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        lengths = list(map(lambda x: len(x.split()), sentences))
        return max(lengths)