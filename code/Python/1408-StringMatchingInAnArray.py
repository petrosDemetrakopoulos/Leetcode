class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        for i in words:
            for j in words:
                if i != j:
                    if i in j:
                        res.append(i)
        return list(set(res))