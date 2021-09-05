# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # dummy = ListNode(0)
        # pointer = dummy
        if head == None:
            return head
        if head.next == None:
            return head
        
        current = head.next
        prev = head
        while current!=None:
            if prev.val == current.val:
                prev.next = current.next
            else:
                prev=current
            current = current.next

        return head
        