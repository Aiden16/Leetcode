class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        def recur(l,r):
            if l>r:
                return None
            root=TreeNode(max(nums[l:r+1]))
            ind=nums.index(root.val)
            root.left=recur(l,ind-1)
            root.right=recur(ind+1,r)
            return root
        root=recur(0,len(nums)-1)
        return root