# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        t=head
        h=head.next
        while True:
            t=t.next
            if not h.next or not h.next.next:
                break
            h=h.next.next
        return t

        