class Solution(object):
    def sumNumbers(self, root):
        stack=[[root,str(root.val)]]
        res=0
        while stack:
            node,path=stack.pop()
            if node.left:
                stack.append([node.left,path+str(node.left.val)]) #9,49
            if node.right:
                stack.append([node.right,path+str(node.right.val)]) #0 , 40
            
            if not node.left and not node.right:
                res+=int(path)
        return res