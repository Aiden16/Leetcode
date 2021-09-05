# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#use inorder and check if appended value in lis is greater or equal to upcoming value:
    # if yes return False
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        lis=[]
        s=[]
        cur=root
        while True:
            if cur:
                s.append(cur)
                cur=cur.left
            elif s:
                node=s.pop()
                if lis and lis[-1]>=node.val:
                    return False
                lis.append(node.val)
                cur=node.right
            else:
                break
        return True
            