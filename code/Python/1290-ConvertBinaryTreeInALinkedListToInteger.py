# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        bin_str = ''
        res = 0
        while head != None:
            bin_str += str(head.val)
            head = head.next
        
        for i in xrange(len(bin_str)):
            res += int(bin_str[i]) * (2 ** (len(bin_str) -1 - i))
        return res