class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # pass
        self.count = 0
        def recur(root,path,h):
            if not root:
                return
            path += root.val
            if path == targetSum:
                self.count+=1
            if path-targetSum in h:
                self.count+=h[path-targetSum]
            h[path] = h.get(path,0)+1
            left = recur(root.left,path,h)
            right = recur(root.right,path,h)
            if path in h:
                h[path]-=1
                if h[path]<=0:
                    del h[path]
        recur(root,0,{})
        return self.count