class Solution:
    def possibleBipartition(self, n: int, d: List[List[int]]) -> bool:
        
        #use graph coloring
        adj={}
        colors=[-1 for i in range(1,n+1)]
        # to=[]
        for like,dislike in d:
            if like in adj:
                adj[like].append(dislike)
            else:
                adj[like]=[dislike]
            if dislike in adj:
                adj[dislike].append(like)
            else:
                adj[dislike]=[like]
        to=list(adj.keys())
        seen=set()
        for i in range(1,n+1):
            if i not in seen:
                qu=deque([i])
                colors[i-1]=0
            else:
                continue
            while qu:
                node = qu.popleft()
                seen.add(node)
                c=colors[node-1]
                if node in adj:
                    for nei in adj[node]:
                        if nei in seen:
                            if c==colors[nei-1]:
                                return False
                        else:
                            if c==0:
                                colors[nei-1]=1
                            else:
                                colors[nei-1]=0
                            qu.append(nei)
                            seen.add(nei)
        return True