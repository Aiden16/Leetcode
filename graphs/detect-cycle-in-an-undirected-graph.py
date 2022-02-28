from collections import deque
class Solution:
    
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V, adj):
	    visited = set()
	    def dfs(node,p):
	        visited.add(node)
	        for nei in adj[node]:
	            
	            if nei not in visited:
	                if dfs(nei,node):
	                    return True
	            else:
	                
	                if nei!=p:
	                    print(nei,p)
	                    return True
	        return False
	    for node in range(V):
	        if node not in visited:
	            if dfs(node,-1):
	                return 1 
	    return 0
	    #bfs implementation
        def bfs(node):
            visited = set()
            qu = deque([node])
            upcoming = set()
            while qu:
                for i in range(len(qu)):
                    node = qu.popleft()
                    if node in visited:
                        return True
                    visited.add(node)
                    for nei in adj[node]:
                        if nei not in visited:
                            qu.append(nei)
            return False
        for node in range(V):
            if bfs(node):
                return 1
        return 0