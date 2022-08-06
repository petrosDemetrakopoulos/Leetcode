class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        cnt = 0
        for i in range(len(expected)):
            if expected[i] != heights[i]:
                cnt += 1
        return cnt