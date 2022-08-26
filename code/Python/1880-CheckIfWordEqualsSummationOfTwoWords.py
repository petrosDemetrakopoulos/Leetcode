class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        """
        :type firstWord: str
        :type secondWord: str
        :type targetWord: str
        :rtype: bool
        """
        ab = 'abcdefghijklmnopqrstuvwxyz'
        num1 = ''
        num2 = ''
        target = ''
        for char in firstWord:
            num1 += str(ab.index(char))
        
        for char in secondWord:
            num2 += str(ab.index(char))
            
        for char in targetWord:
            target += str(ab.index(char))

        return (int(num1) + int(num2)) == int(target)