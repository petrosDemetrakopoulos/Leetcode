class Solution(object):
    def calcFib(self,n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.calcFib(n-1) + self.calcFib(n-2)

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.calcFib(n)