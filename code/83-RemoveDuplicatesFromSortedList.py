# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        crn_node = head
        if crn_node is None:
            return
        while crn_node.next is not None:
            if crn_node.val == crn_node.next.val:
                new = crn_node.next.next
                crn_node.next = None
                crn_node.next = new
            else:
                crn_node = crn_node.next
        return head