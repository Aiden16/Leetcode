# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        lis=[]
        q1=[root1]
        q2=[root2]
        while q1 or q2:
            if q1:
                n1=q1.pop(0)
                if n1:
                    lis.append(n1.val)
            if q2:
                n2=q2.pop(0)
                if n2:
                    lis.append(n2.val)
            if n1:
                if n1.left:
                    q1.append(n1.left)
                if n1.right:
                    q1.append(n1.right)
            if n2:
                if n2.left:
                    q2.append(n2.left)
                if n2.right:
                    q2.append(n2.right)
        lis.sort()
        return lis
            
        