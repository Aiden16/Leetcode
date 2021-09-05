# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        arr=[]
        slow=fast=head
        cur=head
        count=0
        while cur:
            count+=1
            cur=cur.next
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        link=slow
        while slow:
            slow=slow.next
            if slow:
                arr.append(slow)
        link.next=None
        cur=head
        next_node=cur.next
        while arr:
            next_node=cur.next
            ele=arr.pop()
            cur.next=ele
            ele.next=next_node
            cur=next_node

