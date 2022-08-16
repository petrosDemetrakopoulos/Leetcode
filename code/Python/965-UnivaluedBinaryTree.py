# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traverse(self, root, value):
        if root==None:
            return True
        if root.val != value:
            return False
        return self.traverse(root.left, value) and self.traverse(root.right, value)
        
        
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.traverse(root, root.val)