class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        pos_c = []
        res = []
        for i in xrange(len(s)):
            if s[i] == c:
                pos_c.append(i)
        
        for i in xrange(len(s)):
            min_abs = len(s)
            for j in xrange(len(pos_c)):
                if abs(i-pos_c[j]) < min_abs:
                    min_abs = abs(i-pos_c[j])
            res.append(min_abs)
        return res