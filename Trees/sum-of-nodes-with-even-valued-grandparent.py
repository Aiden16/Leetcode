# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        family={}
        count=0
        family[root]=None
        q=collections.deque([root])
        temp=[]
        while q:
            for i in range(len(q)):
                n=q.popleft()
                temp.append(n)
                if n.left:
                    family[n.left]=n
                    q.append(n.left)
                if n.right:
                    family[n.right]=n
                    q.append(n.right)
            if family[temp[0]]!=root and family[temp[0]]:
                for node in temp:
                    if family[family[node]].val%2==0:
                        count+=node.val
            temp=[]
        return count
                
#another approach
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        count=0
        q=[[root,None,None]]
        temp=[]
        while q:
            for i in range(len(q)):
                n,p,g=q.pop(0)
                if n and p and g and g.val%2==0:
                    temp.append([n.val,p.val,g.val])
                if n.left:
                    q.append([n.left,n,p])
                if n.right:
                    q.append([n.right,n,p])
            for i in range(len(temp)):
                count+=temp[i][0]
            temp=[]
        return count
                
        