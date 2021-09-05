class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummyNode = ListNode(0,head)
        prev,curr = dummyNode,head
        while curr!=None and curr.next!=None:
            nxtPtr = curr.next.next
            second = curr.next
            #swap pairs
            second.next = curr
            curr.next = nxtPtr
            prev.next = second
            
            #update pointers
            prev = curr
            curr = nxtPtr
        return dummyNode.next