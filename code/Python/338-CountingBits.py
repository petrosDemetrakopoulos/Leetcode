class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for i in range(n+1):
            bin_n = str(bin(i))[2:]
            cnt = 0
            for j in bin_n:
                if j == '1':
                    cnt+= 1
            res.append(cnt)
        return res