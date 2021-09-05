# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        q=[root]
        temp=[]
        dic={}
        while q:
            for i in range(len(q)):
                node=q.pop(0)
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            for ind,val in enumerate(temp):
                if val not in dic:
                    dic[k-val]=ind
                else:
                    return True
            temp=[]
        return False
                
        