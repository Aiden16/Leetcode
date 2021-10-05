# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def lin(head):
            if not head:
                return ''
            return str(head.val)+lin(head.next)
        link=lin(head)
        qu=deque([[root,str(root.val)]])
        while qu:
            node,path=qu.popleft()
            if node.left:
                qu.append([node.left,path+str(node.left.val)])
            if node.right:
                qu.append([node.right,path+str(node.right.val)])
            if link in path:
                return True
        return False