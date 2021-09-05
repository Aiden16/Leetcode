# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if not root:
            return
        ans=[]
        stack=[[root,root.val,str(root.val)]]
        while stack:
            node,s,path=stack.pop()
            if node.right:
                stack.append([node.right,s+node.right.val,path+'->'+str(node.right.val)])
            if node.left:
                stack.append([node.left,s+node.left.val,path+'->'+str(node.left.val)])
            if not node.left and not node.right:
                if s==targetSum:
                    ans.append(path.split('->'))
        return ans
        