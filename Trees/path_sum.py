# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return
        stack=[[root,root.val]]
        # s,x=stack.pop()
        # print(x)
        # print(stack.pop())
        while stack:
            node,s=stack.pop()
            if node.right:
                stack.append([node.right,s+node.right.val])
            if node.left:
                stack.append([node.left,s+node.left.val])
            if not node.left and not node.right:
                if s==targetSum:
                    return True
        return False