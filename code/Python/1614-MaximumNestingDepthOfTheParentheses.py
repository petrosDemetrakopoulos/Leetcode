class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        tot = 0
        for i in s:
            if i == '(':
                stack.append('(')
                if len(stack) > tot:
                    tot = len(stack)
            elif i == ')':
                stack.pop()
        return tot