
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 
        qu=deque([root])
        while qu:
            node=qu.popleft()
            if node:
                if not node.left and not node.right: #if leaf node, continue to next iteration
                    continue
                if node.left or node.right: #swap left node to right and vice versa
                    tmp=node.left
                    node.left=node.right
                    node.right=tmp
                qu.append(node.left)
                qu.append(node.right)
        return root