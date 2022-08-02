class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            low = 0
            high = len(row) - 1
            mid = 0

            while low <= high:
                mid = (high + low) // 2
                if row[mid] < target:
                    low = mid + 1
                elif row[mid] > target:
                    high = mid - 1
                else:
                    return True
        return False