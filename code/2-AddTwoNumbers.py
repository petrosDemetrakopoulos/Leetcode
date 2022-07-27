# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertAfter(self, prev_node, new_data):
 
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
  
        new_node = ListNode(new_data, prev_node.next)
        prev_node.next = new_node
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        digits_1 = []
        digits_2 = []
        crnNode = l1
        while crnNode != None:
            digits_1.append(crnNode.val)
            crnNode = crnNode.next
        
        crnNode = l2
        while crnNode != None:
            digits_2.append(crnNode.val)
            crnNode = crnNode.next
        
        digits_1.reverse()
        digits_2.reverse()
        str_digits_1 = ''.join([str(x) for x in digits_1])
        str_digits_2 = ''.join([str(x) for x in digits_2])
        total = int(str_digits_1) + int(str_digits_2)
        result_list = list(str(total))
        result_list.reverse()
        
        res_head = ListNode(result_list[0], None)
        crnNode = res_head
        prev_node = res_head
        for i in range(1,len(result_list)):
            crnNode.next = ListNode(result_list[i], None)
            crnNode = crnNode.next
        return res_head