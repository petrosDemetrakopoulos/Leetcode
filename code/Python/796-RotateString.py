class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        s_list = list(s)
        for i in xrange(len(s)):
            s_list = s_list[1:] + [s_list[0]]
            if s_list == list(goal):
                return True
        return  s_list == list(goal)