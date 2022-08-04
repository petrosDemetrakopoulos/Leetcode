class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        res1 = list(set([x for x in nums1 if x not in nums2]))
        res2 = list(set([x for x in nums2 if x not in nums1]))
        return [res1,res2]