class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels = 'aeiouAEIOU'
        list_s = sentence.split()
        
        for i in xrange(len(list_s)):
            crn_word = list_s[i]
            len_a = i+1
            if crn_word[0] in vowels:
                crn_word += 'ma'
            else:
                temp = crn_word[0]
                crn_word = crn_word[1:]
                print(crn_word)
                crn_word += temp + 'ma'
            crn_word += 'a' * len_a
            list_s[i] = crn_word
        return " ".join(list_s)