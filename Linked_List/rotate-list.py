# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        def reverseI(link,k):
            cur=link
            while k:
                k-=1
                cur=cur.next
            kth=cur
            pre=kth
            cur=link
            while cur!=kth:
                next_node=cur.next
                cur.next=pre
                pre=cur
                cur=next_node
            return pre
        def reverseII(link,k):
            cur=link
            curPrev=cur
            if k:
                while k:
                    k-=1
                    curPrev=cur
                    cur=cur.next
                kth=cur
                prev=None
                while cur:
                    next_node=cur.next
                    cur.next=prev
                    prev=cur
                    cur=next_node
                curPrev.next=prev
            else:
                cur=link
                prev=None
                while cur:
                    next_node=cur.next
                    cur.next=prev
                    prev=cur
                    cur=next_node
                return prev 
        #reverse the whole list
        count=0
        cur=head
        prev=None
        while cur:
            count+=1
            next_node=cur.next
            cur.next=prev
            prev=cur
            cur=next_node
        k=k%count
        new=reverseI(prev,k)
        incase=reverseII(new,k)
        if k==0:
            return incase
        return new
