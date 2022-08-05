# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeSL(self,h1, h2):
        if (h1 == None):
            return h2
        if (h2 == None):
            return h1

        if (h1.val < h2.val):
            h1.next = self.mergeSL(h1.next, h2)
            return h1

        else:
            h2.next = self.mergeSL(h1, h2.next)
            return h2

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return self.mergeSL(list1,list2)