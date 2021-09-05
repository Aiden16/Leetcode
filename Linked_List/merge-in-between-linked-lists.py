# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        # print(list1.val)
        # print(list2.val)
        head1 = list1
        head2 = list2
        counter=0
        f1=True
        f2=True
        while head1 or f1 or f2:
            if counter==a-1:
                var1=head1
                f1=False
            if counter == b+1:
                var2=head1
                f2=False
            counter+=1
            head1 = head1.next
        counter=0
        var1.next = head2
        while head2.next:
            head2=head2.next
        head2.next = var2
        return list1
            
        