# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        res = ''
        if root:
            res += str(root.val)
            if not root.left and root.right:
                res += '()'
            if root.left:
                res += '(' + self.tree2str(root.left) + ')'
            if root.right:
                res += '(' + self.tree2str(root.right) + ')'
        return res