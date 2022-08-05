class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_list = list(s)
        digit_list = list(filter(lambda x: x.isdigit(), s_list))
        distinct = list(set(digit_list))
        distinct.sort(reverse=True)
        if len(distinct) > 1:
            return int(distinct[1])
        else:
            return -1