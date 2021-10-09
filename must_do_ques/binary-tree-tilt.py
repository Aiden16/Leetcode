# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans=0
        def dfs(root):
            if not root:
                return 0
            l=dfs(root.left)
            r=dfs(root.right)
            self.ans+=abs(l-r)
            # print(l,r,root.val)
            return l+r+root.val
        dfs(root)
        return self.ans
        #psost order
        # ele=[]
        # l=0
        # r=0
        # stack=[root]
        # while stack:
        #     node=stack.pop()
        #     ele.append(node.val)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # ele.reverse()
        # print(ele)
        # def post(root):
        #     if not root:
        #         return 0
        #     # if root.left:
        #     #     post(root.left)
        #     # if root.right:
        #     #     post(root.right)
        #     l += return post(root.left) + root.val
        #     # r+= return post(root.right) + root.val
        #     # if left or right:
        #     #     print(left-right)
        #     # sub=post(root.left)-post(root.right)+root.val
        #     # ele.append(sub)
        #     # return sub
        #     # print(root.val)
        # print(post(root))
        # # print(ele)
        