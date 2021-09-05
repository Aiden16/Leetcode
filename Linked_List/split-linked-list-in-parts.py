# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head:
            tmp=[]
            while len(tmp)!=k:
                n=ListNode('')
                tmp.append(n)
            return tmp
        count=0
        cur=head
        while cur:
            count+=1
            cur=cur.next
        extra=count%k
        pair=count//k
        tmp=[]
        cur=head
        while cur:
            if extra!=0:
                counter=pair+1
                extra-=1
            else:
                counter=pair
            tmp.append(cur)
            while counter:
                counter-=1
                prev=cur
                cur=cur.next
            prev.next=None
        if len(tmp)!=k:
            while len(tmp)!=k:
                n=ListNode('')
                tmp.append(n)
        return tmp
    
