# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head.next:
            return True
        if not head:
            return
        lis1=[]
        lis2=[]
        count=0
        cur=head
        while cur:
            count+=1;
            cur=cur.next
        if count%2!=0:
            odd=head
            for i in range((count//2)+1):
                lis1.append(odd.val)
                prev=odd
                odd=odd.next
            for i in range((count//2)+1):
                lis2.append(prev.val)
                prev=prev.next
            lis1.reverse()
            if lis1==lis2:
                return True
            else:
                return False
        cur=head
        for i in range(count//2):
            lis1.append(cur.val)
            cur=cur.next
        for i in range(count//2):
            lis2.append(cur.val)
            cur=cur.next
        lis1.reverse()
        if lis1==lis2:
            return True
        else:
            return False
        
        