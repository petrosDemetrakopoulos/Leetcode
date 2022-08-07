class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet = string.ascii_lowercase
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        hs = {}
        
        for i in range(len(alphabet)):
            hs[alphabet[i]] = morse[i]
        
        trans = []
        for word in words:
            tr = ''
            for char in word:
                tr += hs[char]
            trans.append(tr)
        return len(set(trans))