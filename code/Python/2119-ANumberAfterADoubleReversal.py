class Solution(object):
    def isSameAfterReversals(self, num):
        """
        :type num: int
        :rtype: bool
        """
        reversed1 = int("".join(list(reversed(str(num)))))
        reversed2 = "".join(list(reversed(str(reversed1))))
        return int(reversed2) == num