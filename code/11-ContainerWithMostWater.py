class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        crn_water = 0
        res = 0
        min_height = max(height)
        
        l = 0
        r = len(height) - 1
        
        while l < r:
            crn_water = min(height[l], height[r]) * (r-l)
            if crn_water > res:
                res = crn_water
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return res
    