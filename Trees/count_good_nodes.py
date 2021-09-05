# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #bfs here
        qu=[[root,root.val]]
        good=1
        while qu:
            node,path=qu.pop(0)
            if node!=root:
                if node.val>=path:
                    good+=1
            if node.left:
                qu.append([node.left,max(node.val,path)])
            if node.right:
                qu.append([node.right,max(node.val,path)])
        return good
        