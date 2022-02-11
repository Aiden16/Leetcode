class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        ans = ''

        def recur(root):
            if not root:
                return ''
            if not root:
                return ''
            s = str(root.val)
            left = recur(root.left)
            right = recur(root.right)
            if left == '' and right == '':
                return s
            elif left == '':
                return s+'()'+'('+right+')'
            elif right == "":
                return s+'('+left+')'
            else:
                return s+'('+left+')'+'('+right+')'
            #couldn get the ques
            # if not root.left and not root.right:
            #     return '('+str(root.val)+')'
            # left = recur(root.left)
            # right = recur(root.right)
            # print(root.val,str(root.val)+'('+left+right+')')
            # return str(root.val)+'('+left+right+')'
        return recur(root)