class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        res = 0
        str_num = str(num)
        for i in xrange(len(str_num)):
            sliced = str_num[i:i+k]
            if len(sliced) == k:
                if int(sliced) != 0:
                    if num % int(sliced) == 0:
                        res += 1
        return res