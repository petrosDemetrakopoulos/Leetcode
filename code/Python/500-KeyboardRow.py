class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first = "qwertyuiop" + "qwertyuiop".upper()
        second = "asdfghjkl" + "asdfghjkl".upper()
        third = "zxcvbnm" + "zxcvbnm".upper()
        
        res = []
        
        for word in words:
            all_chars_in_first = True
            all_chars_in_second = True
            all_chars_in_third = True
            for char in word:
                if char not in first:
                    all_chars_in_first = False
                    break
            for char in word:
                if char not in second:
                    all_chars_in_second = False
                    break
            for char in word:
                if char not in third:
                    all_chars_in_third = False
                    break
            if all_chars_in_first or all_chars_in_second or all_chars_in_third:
                res.append(word)
        return res