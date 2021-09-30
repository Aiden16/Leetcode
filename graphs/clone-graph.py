"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        keep track of created copy node,
        run dfs through neighbors creating copy
        
        '''
        #iterative dfs
        if not node:
            return None
        copied=Node(node.val)
        seen={node:copied}
        stack=[node]
        while stack:
            n=stack.pop()
            for neigh in n.neighbors:
                if neigh in seen:
                    seen[n].neighbors.append(seen[neigh])
                else:
                    copy = Node(neigh.val)
                    seen[neigh]=copy
                    stack.append(neigh)
                    seen[n].neighbors.append(seen[neigh])
        return copied
        
        #iterative bfs
        if not node:
            return None
        copied = Node(node.val)
        qu=deque([node])
        seen={node:copied}
        while qu:
            n=qu.popleft()
            for neigh in n.neighbors:
                if neigh in seen:
                    seen[n].neighbors.append(seen[neigh])
                else:
                    copy = Node(neigh.val)
                    seen[neigh]=copy
                    qu.append(neigh)
                    seen[n].neighbors.append(seen[neigh])
        return copied
        
        #recursive dfs
        seen={}
        def dfs(node):
            if node in seen:
                return seen[node]
            copy=Node(node.val)
            seen[node]=copy
            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))
            return copy
        return dfs(node) if node else None