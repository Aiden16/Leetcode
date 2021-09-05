# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q=[[root,0]]
        tmp=[]
        ans=0
        while q:
            for i in range(len(q)):
                node,ind=q.pop(0)
                tmp.append(ind)
                if node.left:
                    q.append([node.left,2*ind])
                if node.right:
                    q.append([node.right,2*ind+1])
            ans=max((tmp[-1]-tmp[0])+1,ans)
            tmp=[]
        return ans
      