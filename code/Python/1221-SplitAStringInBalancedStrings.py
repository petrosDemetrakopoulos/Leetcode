class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        balanced = 0
        for i in s:
            if i == 'R':
                balanced += 1
            elif i == 'L':
                balanced -=1
            if balanced == 0:
                cnt +=1 
        return cnt