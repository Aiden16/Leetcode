class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head==None:
            return None
        if head.next == None:
            return head
        curr = head
        next_node = curr.next
        while next_node!=None:
            temp = curr.val
            curr.val = next_node.val
            next_node.val = temp
            if next_node.next:
                curr = next_node.next
                next_node = curr.next
            else:
                break
        return head