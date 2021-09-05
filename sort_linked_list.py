# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return 
        arr=[]
        cur=head
        while cur:
            arr.append(cur)
            cur=cur.next
        lis=sorted(arr,key=lambda k:k.val)
        for i in range(len(lis)-1):
            lis[i].next=lis[i+1]
        lis[len(lis)-1].next=None
        return lis[0]
            
        