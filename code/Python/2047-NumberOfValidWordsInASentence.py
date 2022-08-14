class Solution(object):
    digits = '0123456789'
    def isValid(self,word):
        last_char = word[len(word)-1]
        for char in xrange(len(word)):
            if word[char] in self.digits:
                return False
            if word.count('-') > 1:
                return False
            elif word.count('-') == 1:
                hyp_index = word.index('-')
                if word[0] == '-' or last_char == '-':
                    return False
                if word[hyp_index - 1] not in string.ascii_lowercase or word[hyp_index + 1] not in string.ascii_lowercase:
                    return False
            puncs = word.count(',') + word.count('.') + word.count('!')
            if puncs > 1:
                return False
            elif puncs == 1:
                if last_char not in '!.,':
                    return False
        return True
            
            
                
    def countValidWords(self, sentence):
        """
        :type sentence: str
        :rtype: int
        """
        res = 0
        s_list = sentence.split()
        for word in s_list:
            if self.isValid(word):
                res += 1
        return res