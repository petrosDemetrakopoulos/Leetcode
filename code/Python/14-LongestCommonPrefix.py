class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        strs = map(lambda x: str(x), strs)
        transposed = zip(*strs)
        for i in xrange(len(transposed)):
            firstChar = transposed[i][0]
            all_same = True
            for j in transposed[i]:
                if j != firstChar:
                    all_same = False
                    return prefix
            if all_same:
                prefix = prefix + firstChar
        return prefix