# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {root.val:None} #node:parent
        hash={} #node : [childs]
        qu=deque([root])
        while qu:
            for i in range(len(qu)):
                node=qu.popleft()
                hash[node.val]=[]
                hash[node.val].append(parents[node.val])
                if node.left:
                    qu.append(node.left)
                    hash[node.val].append(node.left.val)
                    parents[node.left.val]=node.val
                else:
                    hash[node.val].append(None)
                if node.right:
                    hash[node.val].append(node.right.val)
                    parents[node.right.val]=node.val
                    qu.append(node.right)
                else:
                    hash[node.val].append(None)
        visited=set()
        #lets do bfs
        qu=deque([target.val])
        level=0
        while qu:
            if level==k:
                return list(qu)
            for i in range(len(qu)):
                node=qu.popleft()
                visited.add(node)
                for nodes in hash[node]:
                    if nodes!=None and nodes not in visited:
                        qu.append(nodes)
                        visited.add(nodes)
            level+=1
        return []
    
    
#=========================================================================#
        m={}
        self.dfs(root,None,m)
        qu=deque([target.val])
        level=0
        visited=set()
        while qu:
            if level==k:
                return list(qu)
            for i in range(len(qu)):
                node=qu.popleft()
                visited.add(node)
                if m[node][0]!=None and m[node][0] not in visited:
                    visited.add(m[node][0])
                    qu.append(m[node][0])
                if m[node][1]!=None and m[node][1] not in visited:
                    visited.add(m[node][1])
                    qu.append(m[node][1])
                if m[node][2]!=None and m[node][2] not in visited:
                    visited.add(m[node][2])
                    qu.append(m[node][2])
            level+=1
        return []
                
                
        
    def dfs(self, node, parent, m):
        """
        dfs through the tree to construct a adjacent list for each node
        {
            val1 : [parent1, left1, right1],
            val2 : [parent2, left2, right2],....
        }
        """
        if not node:
            return
        arr=[parent,None,None]
        if node.left:
            arr[1]=node.left.val
            self.dfs(node.left,node.val,m)
        if node.right:
            arr[2]=node.right.val
            self.dfs(node.right,node.val,m)
        m[node.val]=arr