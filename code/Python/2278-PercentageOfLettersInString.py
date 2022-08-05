import math
class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        cnt = 0
        for i in s:
            if i == letter:
                cnt += 1
        return int(math.floor((float(cnt)/len(s)) * 100))