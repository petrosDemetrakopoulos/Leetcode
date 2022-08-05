class Solution(object):
    def binary_search(self,arr, low, high, x):
        if high >= low:
            mid = (high + low) // 2
 
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binary_search(arr, low, mid - 1, x)
            else:
                return self.binary_search(arr, mid + 1, high, x)
        else:
            return -1
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for i in xrange(len(matrix)):
            res_line = self.binary_search(matrix[i],0,len(matrix[i]) - 1,target)
            if res_line != -1:
                if matrix[i][res_line] == target:
                    return True
        return False