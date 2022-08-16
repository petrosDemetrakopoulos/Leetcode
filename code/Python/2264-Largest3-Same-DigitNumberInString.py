class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        crn_max = 0
        res = ''
        for i in xrange(len(num)):
            for j in xrange(i,len(num)):
                substr = num[j:j+3]
                if len(substr) == 3 and substr[0] == substr[1] and substr[1] == substr[2]:
                    if int(substr) >= crn_max:
                        crn_max = int(substr)
                        res = substr
        return res