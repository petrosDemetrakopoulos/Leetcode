from itertools import combinations
class Solution(object):
    def filterFun(self,x,n):
        if sum(x) == n: 
            return True 
        else: 
            return False
    
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        comb = list(map(lambda x: list(x), list(combinations([1, 2, 3,4,5,6,7,8,9], k))))
        res = list(filter(lambda x: self.filterFun(x,n), comb))
        return res