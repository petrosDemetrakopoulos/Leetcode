class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        str_list = list(s.split(" "))
        nums = list(filter(lambda x: x.isdigit(), str_list))
        nums = list(map(lambda x: int(x), nums))
        isAscending = True
        crnNum = 0
        for x in xrange(len(nums)):
            for y in xrange(x, len(nums)):
                if nums[x] >= nums[y] and x != y:
                    isAscending = False
        return isAscending