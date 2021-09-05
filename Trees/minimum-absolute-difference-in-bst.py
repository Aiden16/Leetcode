# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack=[]
        cur=root
        arr=[]
        while True:
            if cur:
                stack.append(cur)
                cur=cur.left
            elif stack:
                node=stack.pop()
                arr.append(node.val)
                cur=node.right
            else:
                break
        diff=10**20
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<diff:
                diff=arr[i+1]-arr[i]
        return diff
       