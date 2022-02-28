import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        pq = []
        '(wt,node)'
        print(adj)
        heapq.heappush(pq,(0,0))
        visited = set()
        totalCost = 0
        while pq:
            wt,node = heapq.heappop(pq)
            if node in visited:
                continue
            totalCost+=wt
            visited.add(node)
            for v,w in adj[node]:
                if v not in visited:
                    heapq.heappush(pq,(w,v))
        return totalCost