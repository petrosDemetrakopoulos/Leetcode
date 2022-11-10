from collections import defaultdict
class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        fq= defaultdict( int )
        for w in num:
            fq[w] += 1
        for i in range(len(num)):
            if fq[str(i)] != int(num[i]):
                return False
        return True