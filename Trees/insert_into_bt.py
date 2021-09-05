# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur=root
        while cur:
            if cur.val==val:
                return cur
            if cur.val>val:
                cur=cur.left
            elif cur.val<val:
                cur=cur.right
        return None