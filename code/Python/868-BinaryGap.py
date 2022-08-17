class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        str_bin = bin(n)
        pos = []
        dist = []
        for i in xrange(len(str_bin)):
            if str_bin[i] == '1':
                pos.append(i)
        for i in xrange(len(pos)-1):
            dist.append(pos[i+1] - pos[i])
            
        return max(dist) if len(dist) > 0 else 0