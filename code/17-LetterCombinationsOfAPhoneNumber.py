class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        hm = {'2': 'abc',
             '3': 'def',
             '4':'ghi',
             '5':'jkl',
             '6': 'mno',
             '7': 'pqrs',
             '8': 'tuv',
             '9': 'wxyz'}
        res = []
        
        digs = list(digits)
        letters_lists = []
        
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(hm[digits[0]])
        elif len(digits) == 2:
            num1 = list(hm[digits[0]])
            num2 = list(hm[digits[1]])
            for i in num1:
                for j in num2:
                    res.append(i + j)
        elif len(digits) == 3:
            num1 = list(hm[digits[0]])
            num2 = list(hm[digits[1]])
            num3 = list(hm[digits[2]])
            for i in num1:
                for j in num2:
                     for k in num3:
                        res.append(i + j + k)
        else:
            num1 = list(hm[digits[0]])
            num2 = list(hm[digits[1]])
            num3 = list(hm[digits[2]])
            num4 = list(hm[digits[3]])
            for i in num1:
                for j in num2:
                     for k in num3:
                        for l in num4:
                            res.append(i + j + k + l)
        return res