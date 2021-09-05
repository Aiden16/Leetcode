# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        q=[[root,str(root.val)]]
        count=0
        while q:
            node,path=q.pop(0)
            if node.left:
                q.append([node.left,path+str(node.left.val)])
            if node.right:
                q.append([node.right,path+str(node.right.val)])
            if not node.left and not node.right:
                count+=int(path,2)
        return count
        