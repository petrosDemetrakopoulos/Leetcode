class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mydict = {}
        for i in nums:
            if i not in mydict:
                mydict[i] = 0
        
        for i in nums:
            mydict[i] += 1
        
        for val in xrange(len(mydict.values())):
            if mydict.values()[val] == 1:
                return mydict.keys()[val]