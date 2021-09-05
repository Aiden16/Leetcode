# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA=0
        lenB=0
        curA=headA
        curB=headB
        while curA or curB:
            if curA:
                lenA+=1
                curA=curA.next
            if curB:
                lenB+=1
                curB=curB.next
        curA=headA
        curB=headB
        if lenA>lenB:
            for i in range(lenA-lenB):
                curA=curA.next
        elif lenB>lenA:
            for i in range(lenB-lenA):
                curB=curB.next
        while curA!=curB:
            curA=curA.next
            curB=curB.next
        return curA
                