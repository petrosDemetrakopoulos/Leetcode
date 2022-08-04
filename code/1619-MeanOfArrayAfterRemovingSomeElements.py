class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        rem_len = int(0.05 * len(arr))
        arr.sort()
        arr = arr[rem_len:(len(arr) - rem_len)]
        return float(sum(arr))/float(len(arr))