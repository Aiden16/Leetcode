# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        curr = head
        count=0
        while curr:
            count+=1
            curr = curr.next
        right = (count-k)+1
        curr=head
        if right>=k:
            while curr:
                k-=1
                right-=1
                if k==0:
                    temp = curr.val
                    fixed = curr
                elif right==0:
                    fixed.val = curr.val
                    curr.val = temp
                curr=curr.next
        else:
            while curr:
                k-=1
                right-=1
                if right==0:
                    temp = curr.val
                    fixed = curr
                elif k==0:
                    fixed.val = curr.val
                    curr.val = temp
                curr=curr.next
        return head
        