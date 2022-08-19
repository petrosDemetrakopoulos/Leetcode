# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue = [root]
        res = []
        while len(queue):
            queue_len = len(queue)
            row = 0
            for i in xrange(queue_len):
                crn_lvl = queue.pop(0)
                row += crn_lvl.val
                if crn_lvl.left:
                    queue.append(crn_lvl.left)
                if crn_lvl.right:
                    queue.append(crn_lvl.right)
            res.append(float(row)/queue_len)
        return res