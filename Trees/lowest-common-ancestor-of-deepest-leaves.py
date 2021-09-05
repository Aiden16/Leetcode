# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        dic={root:None}
        dicL={}
        level=1
        q=[root]
        tmp=[]
        if not root.left and not root.right:
            return root
        while q:
            for i in range(len(q)):
                node=q.pop(0)
                tmp.append(node)
                if node.left:
                    dic[node.left]=node
                    q.append(node.left)
                if node.right:
                    dic[node.right]=node
                    q.append(node.right)
            dicL[level]=tmp
            level+=1
            tmp=[]
        if len(dicL[level-1])==1:
            if not dic[node].right or not dic[node].left:
                return node
        ans=[]
        common=root
        if len(dicL[level-1])==2:
            for i in dicL[level-1]:
                child=i
                while True:
                    if dic[child].val in ans:
                        common=dic[child]
                        return dic[child]
                    ans.append(dic[child].val)
                    child=dic[child]
                    if not dic[child]:
                        break
        for i in dicL[level-1]:
            child=i
            while True:
                if dic[child] in ans:
                    if dic[child] is not root: common = dic[child]
                ans.append(dic[child])
                child=dic[child]
                if not dic[child]:
                    break
        for i in ans:
            if ans.count(i)==len(dicL[level-1]):
                return i
        return common
                
