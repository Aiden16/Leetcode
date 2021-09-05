"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return 
        q=[root]
        temp=[]
        while q:
            for i in range(len(q)):
                node=q.pop(0)
                temp.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            temp[-1].next=None
            if len(temp)!=1:
                for i in range(len(temp)-1):
                    temp[i].next=temp[i+1]
            temp=[]
        return root
         
                
                    