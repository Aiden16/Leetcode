class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        ele=[]
        def ino(root):
            if root.left:
                ino(root.left)
            ele.append(root.val)
            if root.right:
                ino(root.right)
            return ele
        ino(root)
        def helper(left,right):
            if left>right:
                return None
            mid=(left+right)//2
            root=TreeNode(ele[mid])
            root.left=helper(left,mid-1)
            root.right=helper(mid+1,right)
            return root
        return helper(0,len(ele)-1)