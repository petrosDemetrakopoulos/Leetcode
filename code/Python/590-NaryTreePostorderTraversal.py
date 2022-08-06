"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorderT(self, root, res):
        if not root: return res
        for child in root.children:
            self.postorderT(child, res)
        res.append(root.val)
        return res
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        return self.postorderT(root, [])