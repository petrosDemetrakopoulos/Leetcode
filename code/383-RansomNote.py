class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        letterDict = {}
        for letter in magazine:
            letterDict[letter] = 0
            
        for letter in magazine:
            letterDict[letter] = letterDict[letter] + 1
        
        canBeConstructed = True
        for character in ransomNote:
            if character in letterDict and letterDict[character] != 0:
                letterDict[character] = letterDict[character] - 1
            else:
                canBeConstructed = False
                break
        return canBeConstructed
            