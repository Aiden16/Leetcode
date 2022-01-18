# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        #recur
        def recur(root):
            if not root:
                return 0 
            left=recur(root.left)
            right=recur(root.right)
            ans=max(left,right)+1
            return ans
        return (recur(root))
    
    #iterative
        if not root:
            return 0
        level=0
        qu=deque([root])
        while qu:
            for i in range(len(qu)):
                node=qu.popleft()
                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            level+=1
        return level