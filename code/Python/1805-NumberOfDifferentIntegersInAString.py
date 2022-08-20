class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        nums = '0123456789'
        num_set = set()
        i = 0
        while i < len(word):
            if word[i] in nums:
                j = 0
                crn_char = word[i]
                num = ''
                while crn_char in nums and (i+j) < len(word):
                    num += crn_char
                    j += 1
                    if i+j < len(word):
                        crn_char = word[i+j]
                i = i+j
                num_set.add(int(num))
            else:
                i += 1
        return len(num_set)