# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #timepass approach
        cur=head
        lis=[]
        while cur:
            lis.append(cur.val)
            cur=cur.next
        for i in range(1,len(lis)):
            key=lis[i]
            j=i-1
            while j>=0 and key<lis[j]:
                lis[j+1]=lis[j]
                j-=1
            lis[j+1]=key
        dummy=ListNode(0)
        p=dummy
        for i in lis:
            p.next=ListNode(i)
            p=p.next
        return dummy.next