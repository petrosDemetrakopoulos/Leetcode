class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        hs = {0: [], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}
        for i in xrange(0,len(rings)-1,2):
            crn_rod_id = int(rings[i+1])
            hs[crn_rod_id].append(rings[i])
        res = 0
        for i in hs.values():
            if 'R' in i and 'G' in i and 'B' in i:
                res += 1
        return res