# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        #algo;-
        '''
        maintain monotonic stack for right subtrees
        '''
        
        root=TreeNode(preorder[0])
        stack=[root]
        for ele in preorder[1:]:
            if ele<stack[-1].val:
                stack[-1].left=TreeNode(ele)
                stack.append(stack[-1].left)
            else:
                while stack and ele>stack[-1].val:
                    last=stack.pop()
                last.right=TreeNode(ele)
                stack.append(last.right)
        return root