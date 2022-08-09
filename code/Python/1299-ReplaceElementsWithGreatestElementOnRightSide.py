class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(arr)):
            if len(arr[i+1:]) > 0:
                max_right = max(arr[i+1:])
                arr[i] = max_right
            else:
                arr[i] = -1
        return arr