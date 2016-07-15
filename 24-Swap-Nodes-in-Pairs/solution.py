# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        if p and p.next:
            temp = p.next
            p.next = p.next.next
            temp.next = p
            head = temp
            
        while p and p.next and p.next.next:
            self.swap(p)
            p = p.next.next
            
        return head
            
    def swap(self,cur):
        next_node = cur.next
        next_next = next_node.next
        next_next_next = next_next.next
        cur.next = next_next
        next_next.next = next_node
        next_node.next = next_next_next