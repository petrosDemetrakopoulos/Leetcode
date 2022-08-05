class Solution(object):
    def binarySearch(self,arr, l, r, x):
        if r >= l:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return mid
            elif arr[mid] > x:
                return self.binarySearch(arr, l, mid-1, x)
            else:
                return self.binarySearch(arr, mid + 1, r, x)
        else:
            return -1
    
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = self.binarySearch(nums,0,len(nums)-1,target)
        if res == -1:
            if target > nums[len(nums)-1]:
                return len(nums)
            else:
                i = 0
                k = nums[0]
                if k > target:
                    return 0
                while k <= target and i < len(nums):
                    k = nums[i]
                    i += 1
                return i-1
        return res