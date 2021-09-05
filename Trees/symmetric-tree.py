# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root.left and root.right:
            return False
        if not root.right and root.left:
            return False
        if not root.right and not root.left:
            return True
        stack1=[root.left]
        stack2=[root.right]
        ele=[]
        while stack1:
            nodeL=stack1.pop(0)
            if nodeL:
                ele.append(nodeL.val)
                if nodeL.left:
                    stack1.append(nodeL.left)
                else:
                    stack1.append(None)
                if nodeL.right:
                    stack1.append(nodeL.right)
                else:
                    stack1.append(None)
            else:
                ele.append(nodeL)
        ele1=[]
        while stack2:
            nodeR=stack2.pop(0)
            if nodeR:
                ele1.append(nodeR.val)
                if nodeR.right:
                    stack2.append(nodeR.right)
                else:
                    stack2.append(None)
                if nodeR.left:
                    stack2.append(nodeR.left)
                else:
                    stack2.append(None)
            else:
                ele1.append(nodeR)
        return ele==ele1
    
#optimal approach

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #optimal approach
        qu=deque([(root.left,root.right)])
        while qu:
            nodeL,nodeR=qu.popleft()
            if not nodeL and not nodeR:
                continue
            if not nodeL or not nodeR:
                return False
            if nodeL.val!=nodeR.val:
                return False
            qu.append((nodeL.left,nodeR.right))
            qu.append((nodeL.right,nodeR.left))
        return True