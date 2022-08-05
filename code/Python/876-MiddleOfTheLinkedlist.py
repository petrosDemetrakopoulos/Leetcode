import math
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        crnNode = head
        mid = 0
        while crnNode != None:
            crnNode = crnNode.next
            count +=1 
        if count % 2 == 0:
            mid = (count / 2) + 1
        else:
            mid = (count - 1) / 2
            mid += 1
        
        crnNode = head
        for i in xrange(1,mid):
            crnNode = crnNode.next
        return crnNode