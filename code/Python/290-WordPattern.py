class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        plist = list(pattern)
        hash_tbl = {}
        slist = s.split()
        if len(slist) != len(plist):
            return False
        for i in xrange(len(slist)):
            if slist[i] not in hash_tbl and plist[i] not in hash_tbl.values():
                hash_tbl[slist[i]] = plist[i]
            if slist[i] in hash_tbl:
                slist[i] = hash_tbl[slist[i]]
   
        return plist == slist