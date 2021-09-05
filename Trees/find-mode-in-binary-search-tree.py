# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        # pass
        qu=[root]
        m=1
        dic={}
        while qu:
            node=qu.pop(0)
            if node.val in dic:
                dic[node.val]+=1
                m=max(m,dic[node.val])
            else:
                dic[node.val]=1
            if node.left:
                qu.append(node.left)
            if node.right:
                qu.append(node.right)
        ans=[]
        for key,val in dic.items():
            if val==m:
                ans.append(key)
        return ans
            