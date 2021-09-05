# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root.left and not root.right:
            return root
        q=[root]
        dic={root:None}
        dicL={}
        temp=[]
        level=1
        while q:
            for i in range(len(q)):
                node=q.pop(0)
                temp.append(node)
                if node.left:
                    q.append(node.left)
                    dic[node.left]=node
                if node.right:
                    q.append(node.right)
                    dic[node.right]=node
            dicL[level]=temp
            temp=[]
            level+=1
        if len(dicL[level-1])==1 and dic[node].right and dic[node].left:
            return dic[node]
        else:
            if len(dicL[level-1])==1 and (not dic[node].left or not dic[node].right):
                return node
        ans=[]
        for i in dicL[level-1]:
            child=i
            while True:
                ans.append(dic[child])
                child=dic[child]
                if not child:
                    break
        for i in ans:
            if ans.count(i)==len(dicL[level-1]):
                return i
