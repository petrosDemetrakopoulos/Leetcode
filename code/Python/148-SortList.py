import collections
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst = []
        crn = head
        while crn:
            lst.append(crn.val)
            crn = crn.next
        lst.sort()
        lst = collections.deque(lst)

        crn = head
        while crn:
            crn.val = lst.popleft()
            crn = crn.next
        return head