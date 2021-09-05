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
        tmp=[]
        while qu:
            for i in range(len(qu)):
                node=qu.pop(0)
                tmp.append(node)
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            tmp[-1].next=None
            for i in range(len(tmp)-1):
                tmp[i].next=tmp[i+1]
            tmp=[]
        return root
        