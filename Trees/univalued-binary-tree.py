# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        s=[root]
        c=root.val
        while s:
            node=s.pop()
            if node.val!=c:
                return False
            if node.right:
                s.append(node.right)
            if node.left:
                s.append(node.left)
        return True
    