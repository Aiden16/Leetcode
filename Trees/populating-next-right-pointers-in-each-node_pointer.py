"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        qu=[root]
        while qu:
            node=qu.pop(0)
            if node.left and node.right:
                node.left.next=node.right
                if node.next:
                    node.right.next=node.next.left
                qu.append(node.left)
                qu.append(node.right)
        return root
