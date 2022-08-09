# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfsInvert(self,root):
        if not root: return
        left = self.dfsInvert(root.left)
        right = self.dfsInvert(root.right)
        root.left, root.right = root.right, root.left
        return root
        
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.dfsInvert(root)