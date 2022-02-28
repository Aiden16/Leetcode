# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def recur(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val!=root2.val:
                return False
            invert = recur(root1.left,root2.right) and recur(root1.right,root2.left)
            notInvert = recur(root1.left,root2.left) and recur(root1.right,root2.right)
            return invert or notInvert
        return recur(root1,root2)