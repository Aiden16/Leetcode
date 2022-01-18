
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # self.ans=0
        def recur(root):
            if not root:return 0
            level=0
            for i in root.children:
                level=max(recur(i),level)
            return level+1