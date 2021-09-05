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
        dummy = ListNode(0,head)
        # dummy.next = head
        prev = dummy

        # dummy.next = head
        print(dummy)
        while head!=None:
            if head.next!=None and head.val == head.next.val:
                while head.next!=None and head.val==head.next.val:
                    head=head.next
                prev.next = head.next
            else:
                prev = head
            head = head.next
        return dummy.next
        
#         current = head.next
#         prev = head
#         nextNode=current.next
#         while nextNode!=None:
#             if current.val == nextNode.val:
#                 while(current.val==nextNode.val and nextNode!=None):
#                     print('while')
#                     current = current.next
#                     nextNode = current.next
#                     prev.next = nextNode
#                     # print(prev.next.val)
#             else:
#                 prev = current.next

#             current = current.next
#             nextNode = current.next
#         #     else:
#         #         prev=current
#         #     current = current.next
 # pointer = dummy
#         if head == None:
#             return head
#         if head.next == None:
#             return head
        
#         current = head.next
#         prev = head
#         while current!=None:
#             if prev.val == current.val:
#                 prev.next = current.next.next
#             else:
#                 prev=current
#             current = current.next

#         return head
    

        # return head
        