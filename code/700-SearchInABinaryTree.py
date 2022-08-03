# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        crn_node = root
        while crn_node.val != val:
            if val < crn_node.val:
                if crn_node.left:
                    crn_node = crn_node.left
                else:
                    return None
            elif val > crn_node.val:
                if crn_node.right:
                    crn_node = crn_node.right
                else:
                    return None
            else:
                return crn_node
        return crn_node