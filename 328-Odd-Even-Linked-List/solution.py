# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        
        odd_head = head
        even_head = head.next
        even = even_head
        while even_head and even_head.next:
            odd_head.next = even_head.next
            odd_head = odd_head.next
            even_head.next = odd_head.next
            even_head = even_head.next
        
        odd_head.next = even
        return head
        