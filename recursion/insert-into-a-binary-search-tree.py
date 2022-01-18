# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        def recur(root,val):
            if not root:
                return TreeNode(val)
            if val<root.val:
                root.left = recur(root.left,val)
            else:
                root.right = recur(root.right,val)
            
            return root
        return recur(root,val)
        #brute recursive soln
        
        # def recur(root,val):
        #     if not root.left and not root.right:
        #         if val>root.val:
        #             root.right = TreeNode(val)
        #         else:
        #             root.left = TreeNode(val)
        #         return 
        #     if val>root.val:
        #         if root.right:
        #             recur(root.right,val)
        #         else:
        #             root.right = TreeNode(val)
        #     else:
        #         if root.left:
        #             recur(root.left,val)
        #         else:
        #             root.left = TreeNode(val)
        # recur(root,val)
        # return root