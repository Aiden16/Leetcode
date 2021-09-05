# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return 
        ele=[]
        def inord(root):
            if root.left:
                inord(root.left)
            ele.append(root.val)
            
            if root.right:
                inord(root.right)
            
            return ele
        return inord(root)
        