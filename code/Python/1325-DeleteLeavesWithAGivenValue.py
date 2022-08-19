# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traverse(self, root, target):
        if root == None:
            return None
        root.left = self.traverse(root.left, target)
        root.right = self.traverse(root.right, target)
        if root.left == None and root.right == None and root.val == target:
            return None
        return root
        
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        return self.traverse(root,target)