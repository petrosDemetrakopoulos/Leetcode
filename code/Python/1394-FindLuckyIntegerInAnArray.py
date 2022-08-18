class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        max_res = -1
        for i in arr:
            if i == arr.count(i) and i > max_res:
                max_res = i
        return max_res
        