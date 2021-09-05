# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        print(val)
        new=TreeNode(val)
        cur=root
        prev=cur
        if not root:
            root=new
            return root
        while True:
            if cur.val>new.val:
                prev=cur
                cur=cur.left
                if not cur:
                    prev.left=new
                    break
            if cur.val<new.val:
                prev=cur
                cur=cur.right
                if not cur:
                    prev.right=new
                    break
        return root
                        
            
        