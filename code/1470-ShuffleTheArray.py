class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        list1 = nums[:len(nums)//2]
        list2 = nums[len(nums)//2:]
        res = []
        j = 0 
        k = 0
        for i in xrange(0, 2*n):
            if i % 2 == 0:
                res.append(list1[j])
                j += 1
            else:
                res.append(list2[k])
                k+=1
        return res