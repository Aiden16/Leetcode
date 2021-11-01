class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adj={}
        color=[-1 for i in range(len(graph))]
        for i,nodes in enumerate(graph):
            adj[i]=nodes
        qu=None
        seen=set()
        for i in range(len(graph)): 
            if i not in seen:
                qu=[i]
                color[i]=0
            else:
                continue
            while qu:
                node=qu.pop(0)
                seen.add(node)
                c=color[node]
                for n in adj[node]:
                    if n in seen:
                        if c==color[n]:
                            return False
                    else:
                        if c==0:
                            color[n]=1
                            seen.add(n)
                        else:
                            color[n]=0
                            seen.add(n)
                        qu.append(n)
        return True
                            
                    