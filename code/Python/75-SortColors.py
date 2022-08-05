class Solution(object):
    def partition(self,l, r, nums):
        pivot, ptr = nums[r], l
        for i in xrange(l, r):
            if nums[i] <= pivot:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1

        nums[ptr], nums[r] = nums[r], nums[ptr]
        return ptr
 
    def quicksort(self,l, r, nums):
        if len(nums) == 1:  
            return nums
        if l < r:
            pi = self.partition(l, r, nums)
            self.quicksort(l, pi-1, nums)  
            self.quicksort(pi+1, r, nums)  
        return nums
    
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        print(self.quicksort(0, len(nums)-1, nums))