# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        counter=0
        print(head)
        curr = head
        while curr!=None:
            counter+=1
            curr=curr.next
        if counter%2==0:
            counter=(counter//2)+1
        else:
            counter=(counter//2)+1
        current = head
        while(counter>1):
            counter-=1
            current = current.next
        return current
            
        