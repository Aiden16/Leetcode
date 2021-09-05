# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ele=[]
        if root:
            ele+=self.postorderTraversal(root.left)
            ele+=self.postorderTraversal(root.right)
            ele.append(root.val)
        return ele
            
        # if root is None:
        #     return root
        # s1=[]
        # s2=[]
        # s1.append(root)
        # while(len(s1)>0):
        #     root=s1.pop()
        #     s2.append(root.val)
        #     if root.left:
        #         s1.append(root.left)
        #     if root.right:
        #         s1.append(root.right)
        # s2.reverse()
        # return s2
        