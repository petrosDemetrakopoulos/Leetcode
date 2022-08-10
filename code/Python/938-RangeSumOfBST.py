# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    total = 0
    def traverse(self, root,low,high):
        if root==None:
            return self.total
        if root.val in range(low, high+1):
            self.total += root.val
            print(self.total)
        self.traverse(root.left,low,high)
        self.traverse(root.right,low,high)
        
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.traverse(root,low,high)
        return self.total