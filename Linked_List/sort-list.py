# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        def merge(l,r):
            dummy = ListNode(0)
            tail = dummy
            p1,p2 = l,r
            while p1 and p2:
                if p1.val<p2.val:
                    tail.next = p1
                    p1 = p1.next
                else:
                    tail.next = p2
                    p2 = p2.next
                tail = tail.next
            if p1:
                tail.next = p1
            if p2:
                tail.next = p2
            return dummy.next
        
        
        def getMid(head):
            s,f = head,head
            prev=s
            while f and f.next:
                f=f.next.next
                prev = s
                s=s.next
            prev.next = None
            return s
        
        def mergeSort(head):
            if not head or not head.next:
                return head
            mid = getMid(head)
            left = mergeSort(head)
            right = mergeSort(mid)
            return merge(left,right)
        return mergeSort(head)