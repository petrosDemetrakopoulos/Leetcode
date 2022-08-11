# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.val)
            res = res + self.inorderTraversal(root.right)
        return res
    
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        hs = {}
        resp = self.inorderTraversal(root)
        res = []
        for i in resp:
            hs[i] = resp.count(i)

        mode = max(hs.values())
        for i in range(len(hs.values())):
            if hs.values()[i] == mode:
                res.append(hs.keys()[i])
        return res