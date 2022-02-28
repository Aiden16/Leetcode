import heapq
class Solution:
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V, adj, S):
        #code here
        pq = []
        'wt,node'
        heapq.heappush(pq,(0,S))
        visited = set()
        ans = []
        ans = [0]*V
        while pq:
            wt,node = heapq.heappop(pq)
            if node in visited:
                continue
            ans[node]=wt
            visited.add(node)
            for nei,w in adj[node]:
                if nei not in visited:
                    heapq.heappush(pq,(wt+w,nei))
            
        return ans