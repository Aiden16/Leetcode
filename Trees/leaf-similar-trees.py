# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        arr1=[]
        arr2=[]
        def post(root,arr):
            if not root:
                return 0
            if root.left:
                post(root.left,arr)
            if root.right:
                post(root.right,arr)
            if not root.left and not root.right:
                arr.append(root.val)
            return arr
        post(root1,arr1)
        post(root2,arr2)
        return arr1==arr2
        