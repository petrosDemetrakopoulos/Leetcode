class Solution(object):
    def cellsInRange(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        start_stop = s.split(":")
        start, stop = start_stop[0], start_stop[1]
        start_num = int(start[1:])
        end_num = int(stop[1:])
        start_col = (start[:1])
        end_col = (stop[:1])
        res = []
        for i in xrange(ord(start_col), ord(end_col) + 1):
            crn_col = chr(i)
            for j in xrange(start_num,end_num+1):
                res.append(crn_col + str(j))
        return res