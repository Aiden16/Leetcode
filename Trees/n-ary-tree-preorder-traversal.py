"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return 
        ans=[]
        stack=[root]
        while stack:
            node=stack.pop()
            ans.append(node.val)
            if node.children:
                tmp=node.children[::-1]
                for i in tmp:
                    stack.append(i)
        return ans
            
            
        
        