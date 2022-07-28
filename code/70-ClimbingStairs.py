class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        temp = [1,2]
        if n <= 2:
            return temp[n-1]
        for i in range(2,n):
            temp.append(temp[i-1] + temp[i-2])
        return temp.pop()