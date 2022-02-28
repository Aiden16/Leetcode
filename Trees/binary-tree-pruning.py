class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def recur(root):
            if not root:
                return
            root.left = recur(root.left)
            root.right = recur(root.right)
            if root.val == 0 and not root.left and not root.right:
                return None
            return root
        return recur(root)
        