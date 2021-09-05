# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        q=[root]
        stack=[]
        cur=root
        count=0
        #to count total val
        while True:
            if cur:
                stack.append(cur)
                cur=cur.left
            elif stack:
                node=stack.pop()
                count+=node.val
                cur = node.right
            else:
                break
        #to compute each node val
        cur=root
        var=0
        while True:
            if cur:
                stack.append(cur)
                cur=cur.left
            elif stack:
                node=stack.pop()
                bfr=node.val #to keep track of unchanged node
                node.val=count-var #subtract the values of those nodes which hv less val than cur node
                var+=bfr #to keep track of visited node
                cur=node.right
            else:
                break
        return root
                    
        