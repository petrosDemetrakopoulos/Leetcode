from itertools import combinations
from itertools import groupby
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res_set = []
        for i in xrange(len(nums)+1):
            res_set.append(list(map(lambda x: list(x), combinations(nums,i))))
        flat_list = [item for sublist in res_set for item in sublist]
        flat_list.sort()
        # remove duplicates
        return list(flat_list for flat_list,_ in groupby(flat_list))