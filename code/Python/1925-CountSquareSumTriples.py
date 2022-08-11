class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        squaredN = [x*x for x in xrange(1,n+1)]
        cnt = 0
        for a in xrange(1,n+1):
            for b in xrange(1,n+1):
                if a != b:
                    if a **2 + b**2 in squaredN:
                        cnt += 1
        return cnt