# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def traverse(self, root, list_nodes):
        if root==None:
            return
        self.traverse(root.left, list_nodes)
        self.traverse(root.right, list_nodes)
        list_nodes.append(root.val)
    
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.traverse(root, res)
        return res