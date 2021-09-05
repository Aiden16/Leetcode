# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # newRoot = TreeNode(root1.val+root2.val)
        # print(newRoot)
        q1=[root1]
        q2=[root2]
        # while q1 and q2:
        #     node1=q1.pop(0)
        #     node2=q2.pop(0)
        #     if node1.left:
        #         left=node1.left.val
        #         q1.append(node1.left)
        #     if node2.left:
        #         left+=node2.left.val
        #         q2.append(node2.left)
        #     if node1.right:
        #         right=node1.right.val
        #         q1.append(node1.right)
        #     if node2.right:
        #         right+=node2.right.val
        #         q2.append(node2.right)
        #     print('left',left)
        #     print('right',right)
        #     left=0
        #     right=0
            # if left!=0:
            #     root.left=
        
        # preorder approach
        if not root1 and not root2:
            return 
        if not root1:
            return root2
        if not root2:
            return root1
        stack=[root1]
        ele=[]
        newRoot = TreeNode(root1.val)
        cur=newRoot
        s2=[cur]
        while stack:
            node=stack.pop()
            cur=s2.pop()
            ele.append(node.val)
            if node.right:
                stack.append(node.right)
                cur.right=TreeNode(node.right.val)
                s2.append(cur.right)
            if node.left:
                stack.append(node.left)
                cur.left = TreeNode(node.left.val)
                s2.append(cur.left)
            # print('newRoot',cur)
        # print(newRoot)

        # print(newRoot)
        # print(ele)
        # print(point)
            
        # print('helo')
        q1=[newRoot]
        q2=[root2]
        while q1 and q2:
            n1=q1.pop(0)
            n2=q2.pop(0)
            if n1 and n2:
                n1.val+=n2.val
                if not n1.left and n2.left:
                    n1.left = TreeNode(0)
                if not n1.right and n2.right:
                    n1.right = TreeNode(0)
                q1.append(n1.left)
                q1.append(n1.right)
                q2.append(n2.left)
                q2.append(n2.right)
        # print(root1)
        return newRoot

        
