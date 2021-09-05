# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None;
        while head!=None:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev
#         dummy = ListNode(0,head)
#         tail = dummy.next.next
#         current = head.next
#         iterate = head.next
#         prev = head
        
#         while iterate!=None:
#             print('current==>',current.val)
#             print('prev==>',prev.val)
#             current.next = prev
#             current = iterate.next
#             # tail.next = prev
#             prev = iterate
#             iterate = iterate.next