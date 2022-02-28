class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, adj):
        # code here
        def dfs(node):
            visited.add(node)
            order.add(node)
            for nei in adj[node]:
                if nei in visited and nei in order:
                    return True
                elif nei in visited:
                    continue
                else:
                    if dfs(nei):
                        return True
            order.remove(node)
            return False
        visited = set()
        order = set()
        for i in range(V):
            if i not in visited:
                if dfs(i):
                    return 1
        return 0