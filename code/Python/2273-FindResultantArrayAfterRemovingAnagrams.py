class Solution(object):
    def areAnagrams(self,str1,str2):
        return sorted(list(str1)) == sorted(list(str2))
    
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        i = len(words) -1
        while i > 0:
            if self.areAnagrams(words[i],words[i-1]):
                del words[i]
                i = len(words) -1
            else:
                i = i - 1
        return words