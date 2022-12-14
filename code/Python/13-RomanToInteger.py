class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        summ= 0
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i in xrange(len(s)-1,-1,-1):
            num = roman[s[i]]
            if 3*num < summ: 
                summ = summ-num
            else: 
                summ = summ+num
        return summ