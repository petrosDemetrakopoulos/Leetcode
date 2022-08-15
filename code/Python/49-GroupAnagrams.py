class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hs = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in hs:
                hs[key] = []
            hs[key].append(s)
        return hs.values()
                    