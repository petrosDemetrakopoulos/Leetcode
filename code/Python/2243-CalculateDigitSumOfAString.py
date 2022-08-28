class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        groups = []
        while len(s) > k:
            for i in xrange(0,len(s),k):
                groups.append(s[i:i+k])
            sums = map(lambda x: sum(map(lambda y: int(y), list(x))), groups)
            new = reduce(lambda x, y: str(x) + str(y), sums)
            s = str(new)
            groups = []
        return s