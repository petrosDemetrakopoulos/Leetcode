class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        n = 0
        for i in xrange(len(startTime)):
            if queryTime in range(startTime[i], endTime[i]+1):
                n += 1
        return n