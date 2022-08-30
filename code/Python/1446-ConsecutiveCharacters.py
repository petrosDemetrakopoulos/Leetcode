class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 1
        power = 0
        
        for i in xrange(len(s)-1):
            char = s[i]
            j = 1
            crn_char = s[i+j]
            while crn_char == s[i] and (i+j) < len(s):
                j+=1
                if (i+j) < len(s):
                    crn_char = s[i+j]
                
            if j > power:
                power = j
        return power