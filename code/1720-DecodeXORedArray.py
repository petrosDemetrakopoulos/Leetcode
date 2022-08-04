class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        res = [first]
        for i in xrange(len(encoded)):
            res.append(res[i] ^ encoded[i])
        return res