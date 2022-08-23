# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        arr = []
        crn = head
        while crn:
            arr.append(crn.val)
            crn = crn.next
        return arr == list(reversed(arr))