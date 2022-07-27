# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hash_tbl = {}
        crn_node = head
        if crn_node == None:
            return False
        while crn_node.next:
            if crn_node not in hash_tbl:
                hash_tbl[crn_node] = 1
            else:
                return True
            crn_node = crn_node.next
        return False