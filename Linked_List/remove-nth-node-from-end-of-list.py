# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nodeCount=0
        cur=head
        while cur:
            nodeCount+=1
            cur=cur.next
        counter=(nodeCount-n)
        if counter==0:
            return head.next
        cur=head
        prev=head
        while cur and counter:
            counter-=1
            prev=cur
            cur=cur.next
            if counter==0:
                prev.next=cur.next
        return head
        #2 pointer approach
        # dummy=ListNode(0,head)
        # left = dummy
        # right=head
        # while right and n!=0:
        #     right=right.next
        #     n-=1
        # print(right.val)
        # while right:
        #     left=left.next
        #     right=right.next
        # print(left.val)
        # left.next=left.next.next
        # return dummy.next
        # if head==None:
        #     return None
        # if head.next==None:
        #     return None
        # count=0
        # curr=head
        # while curr:
        #     count+=1
        #     curr=curr.next
        # right = (count-n)+1
        # curr= head
        # prev=head
        # if right==1:
        #     # print('lala')
        #     return head.next
        # while curr:
        #     right-=1
        #     if right==0:
        #         prev.next = curr.next
        #         # pass
        #     prev = curr
        #     curr = curr.next
        # return head
                
            
        