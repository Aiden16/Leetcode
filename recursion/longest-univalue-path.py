class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def recur(root):
            # print(root)
            if root:
                if not root.left and not root.right:
                    return [root.val,1]
                left = recur(root.left)
                right = recur(root.right)
                if left and right and left[0] == root.val and right[0] == root.val:
                    self.ans = max(self.ans,right[1]+left[1]+1)
                    return [root.val,max(left[1],right[1])+1]
                if left:
                    if left[0] == root.val:
                        self.ans = max(self.ans,left[1]+1)
                        return [root.val,left[1]+1]
                if right:
                    if right[0] == root.val:
                        self.ans = max(self.ans,right[1]+1)
                        return [root.val,right[1]+1]
                return [root.val,1]
            
        x = recur(root)
        if not x:return 0
        self.ans = max(self.ans,x[1])
        return self.ans-1