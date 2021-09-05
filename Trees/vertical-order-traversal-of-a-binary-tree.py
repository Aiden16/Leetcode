# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q=[[root,0]]
        dic={}
        ins={}
        lis=[]
        while q:
            for i in range(len(q)):
                node,index=q.pop(0)
                if index not in lis:lis.append(index)
                if index in ins:
                    ins[index].append(node.val)
                else:
                    ins[index]=[node.val]
                if node.left:
                    q.append([node.left,index-1])
                if node.right:
                    q.append([node.right,index+1])
            for i in ins.keys():
                if i not in dic:
                    dic[i]=[]
                    ins[i].sort()
                    for v in ins[i]:
                        dic[i].append(v)
                else:
                    ins[i].sort()
                    for v in ins[i]:
                        dic[i].append(v)
            ins={}
        lis.sort()
        ans=[]
        for i in lis:
            ans.append(dic[i])
        return ans
            
        