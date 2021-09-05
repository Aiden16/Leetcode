# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # prev = None
        # while head!=None:
        #     if head.val == left:
        #         prev = head
        #         head = head.next
        #         # next_node = head.next
        #         while head.val!=right:
        #             next_node = head.next
        #             head.next = prev
        #             prev = head
        #             head = next_node
        #     head = head.next
        # print(prev.val)
        # return prev
        if head==None:
            return None
        prev = None
        current = head
        while(m>1):
            prev = current
            current = current.next
            m-=1
            n-=1
        print(prev.val)
        print(current.val)
        connection = prev
        tail = current
        
        while(n>0):
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            n-=1
        print(prev.val)
        if connection!=None:
            connection.next = prev
        else:
            head = prev
        tail.next = current
        return head
        
                    
        