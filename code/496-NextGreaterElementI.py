class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in xrange(len(nums1)):
            greater = -1
            for j in xrange(len(nums2)):
                if nums1[i] == nums2[j]:
                    for k in xrange(j, len(nums2)):
                        if nums2[k] > nums2[j]:
                            greater = nums2[k]
                            break
            res.append(greater)
        return res