# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #use preorder
        if not root:
            return 
        stack=[root]
        pre=[]
        while stack:
            node = stack.pop()
            pre.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        for i in range(len(pre)-1):
            pre[i].right=pre[i+1]
            pre[i].left=None
        return pre[0]