"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorderT(self, root, res):
        if not root: return res
        res.append(root.val)
        for child in root.children:
            self.preorderT(child, res)
        return res
        
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        return self.preorderT(root, [])