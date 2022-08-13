"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorderT(self, root):
        if root == None:
            return 0
        max_depth = 0
        for i in xrange(len(root.children)):
            max_depth = max(max_depth,self.preorderT(root.children[i]))
        return max_depth + 1
    
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return self.preorderT(root)