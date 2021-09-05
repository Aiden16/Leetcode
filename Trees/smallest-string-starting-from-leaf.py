# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        ans=[]
        stack=[[root,chr(root.val+97)]]
        while stack:
            node,path = stack.pop()
            if node.right:
                stack.append([node.right,path+chr(node.right.val+97)])
            if node.left:
                stack.append([node.left,path+chr(node.left.val+97)])
            if not node.left and not node.right:
                ans.append(path[::-1])
        ans.sort()
        return ans[0]
        