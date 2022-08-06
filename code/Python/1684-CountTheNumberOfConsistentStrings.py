class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        cnt = 0
        for i in words:
            only_allowed = True
            for j in i:
                if j not in allowed:
                    only_allowed = False
            cnt += 1 if only_allowed else 0
        return cnt