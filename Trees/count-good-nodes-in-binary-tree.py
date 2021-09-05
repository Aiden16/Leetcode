#optimal approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack=[[root,root.val]]
        count=0
        while stack:
            n,compare=stack.pop()
            if n.val>=compare:
                count+=1
            compare=max(compare,n.val)
            if n.right:
                stack.append([n.right,compare])
            if n.left:
                stack.append([n.left,compare])
        return count



#not optimal


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack=[[root,str(root.val)]]
        count=0
        while stack:
            n,p=stack.pop()
            lis=list(map(int,p.split('->')))
            if n.val==max(lis):
                count+=1
            if n.right:
                stack.append([n.right,p+'->'+str(n.right.val)])
            if n.left:
                stack.append([n.left,p+'->'+str(n.left.val)])
        return count