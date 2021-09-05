# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        # self.ino=[]
class Solution(object):
    def __init__(self):
        self.ino=[]
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        print(root)
        if root:
            self.inorderTraversal(root.left)
            print(root.val)
            self.ino.append(root.val)
            self.inorderTraversal(root.right)
        print(self.ino)
        return self.ino
        


        #other approach
        
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # def __init__(self):
    #     # self.ino=[]
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ele=[]
        # print(root)
        if root:
            ele+=self.inorderTraversal(root.left)
            # print(root.val)
            ele.append(root.val)
            ele+=self.inorderTraversal(root.right)
        # print(self.ino)
        return ele
        