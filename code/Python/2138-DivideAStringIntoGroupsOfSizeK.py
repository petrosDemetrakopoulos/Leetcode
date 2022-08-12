class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        if len(s) % k != 0:
            s = s + fill * (k - (len(s) % k))
        res = []
        for i in xrange(0,len(s),k):
            res.append(s[i:i+k])
        return res