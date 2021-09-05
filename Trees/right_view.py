# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans=[]
        if not root:
            return 
        q=[root]
        temp=[]
        while q:
            for i in range(len(q)):
                node=q.pop(0)
                temp=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(temp)
        return ans            
        # if not root:
        #     return
        # s=[root]
        # ele=[]
        # while s:
        #     node=s.pop()
        #     ele.append(node.val)
        #     if node.right:
        #         s.append(node.right)
        # r=root
        # q=[r]
        # level=0
        # while q:
        #     for i in range(len(q)):
        #         node=q.pop(0)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level+=1
        # # print(level)
        # # print(node.val)
        # if level==len(ele):
        #     return ele
        # else:
        #     ele.append(node.val)
        #     return ele
        # # print(ele)  

        # return ele
        