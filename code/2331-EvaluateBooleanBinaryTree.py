# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self,root):
        if root.val == 3:
            return self.dfs(root.left) and self.dfs(root.right) 
        elif root.val == 2:
            return self.dfs(root.left) or self.dfs(root.right)
        else:
            return root.val 
    
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.dfs(root)