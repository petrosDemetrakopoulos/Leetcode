class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        letters = []
        for i in sentence:
            if i not in letters:
                letters.append(i)
                
        return len(letters) == 26