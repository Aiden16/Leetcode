# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 
        if not root.left:
            return root
        ans=[]
        stack = []
        curr=root
        while True:
            if curr:
                stack.append(curr)
                curr=curr.left
            elif stack:
                curr = stack.pop()
                ans.append(curr)
                curr=curr.right
            else:
                break
        
        print(ans)
        ans[0].left = None
        ans[0].right=ans[1]
        ans[-1].left = None
        ans[-1].right=None
        # print('ans====>',ans[0].val)
        # print(ans[0].left)
        for i in range(1,len(ans)-1):
            ans[i].left=None
            ans[i].right = ans[i+1]
            
        # print('======')
        # print(root)
        # return ans
        return ans[0]

                    
                
            
        