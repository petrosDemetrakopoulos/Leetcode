class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        res = 0
        for i in xrange(len(arr1)):
            isEl = False
            for j in xrange(len(arr2)):
                if abs(arr1[i]-arr2[j]) <= d:
                    isEl = True
                    break
            if isEl == False:
                res += 1
        return res