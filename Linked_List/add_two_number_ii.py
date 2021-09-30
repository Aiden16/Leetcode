# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #not so efficient soln
        lis1=[]
        lis2=[]
        lis3=[]
        cur1=l1
        cur2=l2
        while cur1 or cur2:
            if cur1:
                lis1.append(cur1.val)
                cur1=cur1.next
            if cur2:
                lis2.append(cur2.val)
                cur2=cur2.next
        lis1.reverse()
        lis2.reverse()
        carry=0
        for i in range(min(len(lis1),len(lis2))):
            val=lis1[i]+lis2[i]+carry
            carry=val//10
            lis3.append(val%10)
        if i<len(lis1):
            for j in range(i+1,len(lis1)):
                val=carry+lis1[j]
                carry=val//10
                lis3.append(val%10)
        if i<len(lis2):
            for j in range(i+1,len(lis2)):
                val=lis2[j]+carry
                carry=val//10
                lis3.append(val%10)
        if carry:
            lis3.append(carry)
        lis3.reverse()
        head=ListNode(lis3[0])
        cur=head
        for i in range(1,len(lis3)):
            cur.next=ListNode(lis3[i])
            cur=cur.next
        return head
            