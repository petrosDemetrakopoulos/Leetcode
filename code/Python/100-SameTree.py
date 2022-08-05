# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recIsSame(self,p,q):
        if(p == None and q == None):
            return True
        if (p == None and q != None):
            return False
        if (q == None and p != None):
            return False
        if(p.val == q.val):
            return self.recIsSame(p.left,q.left) and self.recIsSame(p.right,q.right)
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.recIsSame(p,q)