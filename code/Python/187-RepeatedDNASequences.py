class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        hs = {}
        res = []
        for i in xrange(len(s)-9):
            crn_sub = s[i:i+10]
            if crn_sub not in hs:
                hs[crn_sub] = 1
            else:
                hs[crn_sub] += 1
            if hs[crn_sub] > 1:
                res.append(crn_sub)
        return list(set(res))