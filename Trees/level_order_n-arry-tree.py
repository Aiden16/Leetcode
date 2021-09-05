"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        if not root.children:
            return [[root.val]]
        q=[root.children]
        tmp=[]
        bfs=[[root.val]]
        while q:
            for i in range(len(q)):
                node=q.pop(0)
                for n in node:
                    tmp.append(n.val)
                    if n.children:
                        q.append(n.children)
            bfs.append(tmp)
            tmp=[]
        return bfs
        