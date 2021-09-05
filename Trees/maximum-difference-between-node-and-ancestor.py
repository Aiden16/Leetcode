# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        qu=[[root,root.val,root.val]]
        ans=0
        while qu:
            node,maximum,minimum=qu.pop(0)
            diff=abs(maximum-minimum)
            ans=max(ans,diff)
            if node.left:
                qu.append([node.left,max(node.left.val,maximum),min(node.left.val,minimum)])
            if node.right:
                qu.append([node.right,max(node.right.val,maximum),min(node.right.val,minimum)])  
        return ans