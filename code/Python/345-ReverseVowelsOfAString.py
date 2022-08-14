class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s_list = list(s)
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s_vowels = filter(lambda x: x in vowels, s_list)
        s_vowels.reverse()
        
        k = 0
        for i in xrange(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = s_vowels[k]
                k+=1
        return "".join(s_list)