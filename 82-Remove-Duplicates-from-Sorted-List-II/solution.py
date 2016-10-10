# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        fake_head = ListNode(0)
        fake_head.next = head
        pre = fake_head
        cur = head
        while cur is not None:
            while cur.next is not None and cur.val == cur.next.val:
                cur = cur.next
            if pre.next is cur:
                pre = pre.next
            else:
                pre.next = cur.next
            cur = cur.next

        return fake_head.next