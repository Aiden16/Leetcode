# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        # pass
        sub = []
        h = {}
        def sub_tree(root):
            if not root:
                return ''
            left = sub_tree(root.left)
            right = sub_tree(root.right)
            sub = str(root.val)+'$'+left+'#'+right
            if sub not in h:
                h[sub] = [root,1]
            else:
                h[sub][1] +=1 
            return sub
        sub_tree(root)
        for i in h.keys():
            if h[i][1]>1:
                sub.append(h[i][0])
        return sub