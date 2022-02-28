class Solution:
    def validateBinaryTreeNodes(self, n: int, l: List[int], r: List[int]) -> bool:
        root = 0
        childrens = set(l+r)
        for i in range(n):
            if i not in childrens:
                root = i
        visited = set()
        self.flag = True
        def dfs(node):
            if node in visited:
                self.flag = False
                return
            visited.add(node)
            if l[node]!=-1:
                dfs(l[node])
            if r[node]!=-1:
                dfs(r[node])
        dfs(root)
        if len(visited)<n:
            # print('-----')
            return False
        return self.flag
            