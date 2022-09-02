class Solution(object):
    def gcd (self,a,b):
        if (b == 0):
            return a
        else:
            return self.gcd (b, a % b)

    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.gcd(min(nums),max(nums))