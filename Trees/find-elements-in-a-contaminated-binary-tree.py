# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: TreeNode):
        self.ele=set()
        root.val=0
        qu=deque([root])
        while qu:
            node=qu.popleft()
            self.ele.add(node.val)
            if node.left:
                node.left.val=(node.val*2)+1
                qu.append(node.left)
            if node.right:
                node.right.val = (node.val*2)+2
                qu.append(node.right)
        

    def find(self, target: int) -> bool:
        return target in self.ele
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)