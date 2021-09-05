# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur=head
        fast=cur.next.next
        con=cur.next
        count=0
        while cur and cur.next.next:
            next_node=cur.next
            cur.next=fast
            cur=next_node
            fast=cur.next.next
            count+=1
        if count%2!=0:
            temp=cur.next
            cur.next=None
            temp.next=con
        else:
            cur.next=con
        return head
            
            
        