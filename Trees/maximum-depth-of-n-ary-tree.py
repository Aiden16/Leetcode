# maximum-depth-of-n-ary-tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        q=[root]
        if not root:
            return 0
        if not root.children:
            return 1
        level=1
        while q:
            for i in range(len(q)):
                node=q.pop(0)
                if node.children:
                    for i in node.children:
                        if i.children:
                            q.append(i)
            level+=1
        return level
