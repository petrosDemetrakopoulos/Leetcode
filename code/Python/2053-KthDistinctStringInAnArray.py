class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        dist = filter(lambda x: arr.count(x) == 1, arr)
        if len(dist) < k:
            return ""
        return dist[k-1]