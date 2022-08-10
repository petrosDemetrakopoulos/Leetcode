class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        already_seen = []
        while n != 1:
            n = sum(map(lambda x: int(x) ** 2, list(str(n))))
            if n in already_seen:
                return False
            already_seen.append(n)
        return True