# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #reverse ll
        dummy=ListNode(0,head)
        groupPrev=dummy
        while True:
            kthNode = self.getKth(groupPrev,k)
            if not kthNode:
                break
            groupNext=kthNode.next
            cur,prev=groupPrev.next,kthNode.next
            while cur!=groupNext:
                next_node=cur.next
                cur.next=prev
                prev=cur
                cur=next_node
            tmp=groupPrev.next
            groupPrev.next=kthNode
            groupPrev=tmp
        return dummy.next
    def getKth(self,cur,k):
        while cur and k>0:
            cur=cur.next
            k-=1
        return cur