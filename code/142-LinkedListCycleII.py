# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        crn_node = head
        if crn_node == None:
            return None
        while crn_node.next:
            if crn_node.val == 'T':
                return crn_node
            else:
                crn_node.val = 'T' # set value of visited node to 'T', and for the next nodes we check if the value is set to 'T' (node alreade visited)
            crn_node = crn_node.next # in this way, we achieve O(1) space complexity
        return None