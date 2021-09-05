# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        #iterative soln
        if not root:
            return 
        while root and (root.val<low or root.val>high):
            if root.val<low:root=root.right
            else:root=root.left
        #adjust left subtree
        if not root:
            return
        left=right=root
        while left.left:
            if left.left.val<low:
                left.left=left.left.right
            else:
                left=left.left
        while right.right:
            if right.right.val>high:
                right.right=right.right.left
            else:
                right=right.right
        return root
        pass