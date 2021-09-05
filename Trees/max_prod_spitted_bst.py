# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        elements=[]
        def post(root):
            if not root:
                return 0
            subtree_sum = post(root.left) + post(root.right) + root.val
            elements.append(subtree_sum)
            return subtree_sum
        total_sum=post(root)
        ans=0
        for i in elements:
            prod=i*(total_sum-i)
            ans=max(ans,prod)
        return ans%(10**9+7)

    #iterative soln
    # class Solution(object):
    # def maxProduct(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     dic={None:0}
    #     stack=[[root,0]]
    #     while stack:
    #         node,seen=stack.pop()
    #         if not node:continue
    #         if not seen:
    #             stack+=[[node,1]]
    #             stack+=[[node.left,0]]
    #             stack+=[[node.right,0]]
    #         else:
    #             dic[node]=node.val+dic[node.left]+dic[node.right]
    #     total=dic[root]
    #     ans=0
    #     for i in dic.values():
    #         prod=i*(total-i)
    #         ans=max(ans,prod)
    #     return ans%(10**9+7)
        
