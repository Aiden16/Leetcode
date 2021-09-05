# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        qu=[root]
        dic={}
        while qu:
            node=qu.pop()
            if node.val in dic:
                return True
            else:
                dic[k-node.val]=node
            if node.left:
                qu.append(node.left)
            if node.right:
                qu.append(node.right)
        return False
        