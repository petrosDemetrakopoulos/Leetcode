# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self,rootOr,rootClone, target):
        if rootOr == None or rootClone == None:
            return 
        if rootOr.val == target.val:
            return rootClone
        if rootOr and rootOr.left is None and rootOr.right is None:
            return
    
        res1 = self.dfs(rootOr.left, rootClone.left, target)
        if res1 != None:
            return res1
        res2 = self.dfs(rootOr.right, rootClone.right, target)
        if res2 != None:
            return res2
    
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(original, cloned, target)