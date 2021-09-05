# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head=head
        cur=head
        self.count=0
        while cur:
            self.count+=1
            cur=cur.next
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        r=random.randint(1,self.count)
        cur=self.head
        if r==1:
            return cur.val
        while r!=1:
            cur=cur.next
            r-=1
        return cur.val
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()